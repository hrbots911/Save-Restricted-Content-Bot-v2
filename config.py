# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "20745441"))
API_HASH = getenv("API_HASH", "82c5ac01379b3b8a5603f220d2d406fd")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7990155194").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://hrbots94:c3fSompkz0YxASjR@hruploader.j0chhyv.mongodb.net/?retryWrites=true&w=majority&appName=hruploader")
LOG_GROUP = getenv("LOG_GROUP", "-1002933220325")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002933220325"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "500"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
