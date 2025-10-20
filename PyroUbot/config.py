import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "7638804443").split()))

API_ID = int(os.getenv("API_ID", "20007829"))

API_HASH = os.getenv("API_HASH", "d2f61c499f1e6f12ec1f896f14bcb8f7")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8427967883:AAEnPpli_x_3L3Gppxaby00zJi5D0uNH7uU")

OWNER_ID = int(os.getenv("OWNER_ID", "7638804443"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002312835928").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://zaaytofficial:4MMbEVZLHFBXwbLB@cluster0.mspnbis.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002532309189"))
