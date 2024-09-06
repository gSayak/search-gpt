# To make a search GPT which will search the internet based on the user query and return the results in a chat format

from config.openai_config import client
from typing import List

class SearchGPT:
    def __init__(self):
        self.messages : List = list() # this will store the conversation history
        self.model = "gpt-4o"
        #this will store the search results in a structured format
        self.search_results: List = list()

    def make_openai_call(self):
        pass

    def search_internet(self):
        pass
    
    def get_response(self):
        pass

 

if __name__ == "__main__":
    search_gpt = SearchGPT()
    user_query = "What is the weather in San Francisco?"
    response = search_gpt.get_response(user_query)
    print(response)

