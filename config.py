from os import getenv
from dotenv import load_dotenv

load_dotenv(".env")

BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID") or 0)
API_HASH = getenv("API_HASH")
FSUB = int(getenv("FSUB") or 0)
BOT_NAME = getenv("BOT_NAME")
thumb = getenv("thumb", "https://telegra.ph/file/9f93ca1114a1e01b63239.jpg")
CHANNEL_ID = int(getenv("CHANNEL_ID") or 0)
START_MSG = getenv("START_MSG", "<b>👋Halo {}\n\nSaya Adalah ThumbnailRobot yang akan membantu Anda untuk memasang thumbnail video dengan mudah melalui telegram\n\nKlik button tutorial untuk mulai mengetahui cara-cara nya")
