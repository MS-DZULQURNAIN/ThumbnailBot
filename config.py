from os import getenv
from dotenv import load_dotenv

load_dotenv(".env")

BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID") or 0)
API_HASH = getenv("API_HASH")
FSUB = int(getenv("FSUB") or 0)
BOT_USERNAME = getenv("BOT_USERNAME

