# To make a search GPT which will search the internet based on the user query and return the results in a chat format

# Standard library imports
import json
from typing import List

# Third-party imports
import gradio as gr
import requests

# Local imports
from config.config import SCRAPER_API_KEY as scraper_api_key
from config.openai_config import client
from tools.tools import tools


class SearchGPT:
    def __init__(self):
        self.prompt = "You are a helpful assistant that can search the internet for the user query and return the results in a chat format, help the user with their query. If the user is asking for latest information about anything call the get_user_query tool with the search query as the argument. If the user is asking for anything else that you already know, just answer it. If the user is asking for something you do not know call the get_user_query tool with the search query as the argument and also provide the sources from where the information is fetched in the response after answering the user query. Return the reference links in the response as well."
        self.messages : List = list() # this will store the conversation history
        self.model = "gpt-4o"
        self.tools = tools
        #this will store the search results in a structured format
        self.search_results: List = list()

    def make_openai_call(self):
        response = client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            tools=self.tools,
            tool_choice="auto",
        )
        return response

    def search_internet(self, search_query: str):
        # using scraper api to search the internet
        payload = { 'api_key': scraper_api_key, 'query': search_query, 'num': '2', 'additional_params': 'autoparse=True', 'country_code': 'in' }
        response = requests.get('https://api.scraperapi.com/structured/google/search', params=payload)
        # print(r.text)
        return response.text
    
    def get_response(self, query: str, history):
        self.messages.append({"role": "user", "content": query})
        response = self.make_openai_call()
        self.messages.append(response.choices[0].to_dict()['message'])
        return self.handle_response(response)
    
    def handle_response(self, response):
        tool_calls = response.choices[0].message.tool_calls
        if tool_calls:
            return self.handle_tool_call(tool_calls)
        assistant_response = response.choices[0].message.content
        return assistant_response
    
    def handle_tool_call(self, tool_calls):
        for tool in tool_calls:
            if tool.function.name == "get_user_query":
                search_query = json.loads(tool.function.arguments)['search_query']
                response = self.search_internet(search_query)
                self.messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool.id,
                        "name": tool.function.name,
                        "content": response,
                    }
                )
        response = self.make_openai_call()
        return response.choices[0].message.content

if __name__ == "__main__":
    search_gpt = SearchGPT()

    # Create Gradio interface
    iface = gr.ChatInterface(
        fn=search_gpt.get_response,
        title="SearchGPT",
        description="Ask me anything, and I'll search the internet for you!",
        examples=["What are the trending news in India today?", "Tell me about the latest advancements in AI"],
        theme="soft"
    )
    # Launch the interface
    iface.launch()
