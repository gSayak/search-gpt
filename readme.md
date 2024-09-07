# SearchGPT

SearchGPT is an AI-powered chatbot that can search the internet based on user queries and return results in a conversational format. It combines the power of OpenAI's GPT models with real-time web search capabilities to provide up-to-date information and answers to user questions.

## Features

- Internet search integration using ScraperAPI
- Conversational AI powered by OpenAI's GPT models
- User-friendly chat interface using Gradio
- Ability to provide sources and reference links for information

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- OpenAI API key
- ScraperAPI key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/searchgpt.git
   cd searchgpt
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the root directory and add your API keys:
   ```
   OPEN_AI_KEY=your_openai_api_key_here
   SCRAPER_API_KEY=your_scraper_api_key_here
   ```

## Usage

To run SearchGPT, execute the following command:

```
python main.py
```

This will launch a Gradio interface where you can interact with the chatbot. You can ask questions or request information, and SearchGPT will provide answers based on its knowledge or by searching the internet in real-time.

## Project Structure

- `main.py`: The main script that initializes and runs the SearchGPT chatbot.
- `config/`: Contains configuration files for API keys and OpenAI client setup.
- `tools/`: Defines the tools used by the chatbot, including the internet search function.

## How It Works

1. The user sends a query through the Gradio interface.
2. SearchGPT processes the query using OpenAI's GPT model.
3. If the query requires up-to-date information, SearchGPT uses the ScraperAPI to perform a web search.
4. The search results are then processed and formatted into a conversational response.
5. The response, along with any relevant sources or links, is presented to the user.

## Contributing

Contributions to SearchGPT are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
