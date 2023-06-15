import os


# BOT TOKEN
TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "16452568"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f936697c5c9e5bffd433babef7a4e4c9")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001749379103"))
