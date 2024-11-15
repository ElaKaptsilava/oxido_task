import os

from dotenv import load_dotenv

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'templates')

ARTICLE_PATH = os.path.join(DATA_DIR, 'Zadanie dla JJunior AI Developera - tresc artykulu.txt')
PROMPT_PATH = os.path.join(DATA_DIR, 'prompt.txt')
OUTPUT_PATH = os.path.join(TEMPLATES_DIR, 'output.html')
BASE_TEMPLATE = os.path.join(TEMPLATES_DIR, 'template.html')

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
