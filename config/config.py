import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPEN_AI_KEY")
SCRAPER_API_KEY = os.getenv("SCRAPER_API_KEY")
