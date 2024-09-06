tools = [
     {
        "type": "function",
        "function": {
            "name": "get_user_query",
            "description": "Get the search query from the users message and use a search engine to get the result",
            "parameters": {
                "type": "object",
                "properties": {
                    "search_query": {
                        "type": "string",
                        "description": "The message content provided by the user, e.g., 'What is the weather in San Francisco today?' or 'What is the latest update in the AI space?'"
                    }
                },
                "required": ["search_query"],
                "additionalProperties": False
            }
        }
     }
]