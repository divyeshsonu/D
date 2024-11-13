import os

API_ID    = os.environ.get("API_ID", "28187462")
API_HASH  = os.environ.get("API_HASH", "0159fbade6b803a808fbc5e248d52b87")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7924605822:AAFc7To_ndjnk47DTPZKRu4apXTGYQiXwks") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
