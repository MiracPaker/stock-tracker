import os
import requests

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not TOKEN:
    raise Exception("TELEGRAM_BOT_TOKEN bulunamadı")

if not CHAT_ID:
    raise Exception("TELEGRAM_CHAT_ID bulunamadı")

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

r = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": "✅ Stock Tracker başarıyla çalıştı."
    },
    timeout=30,
)

print(r.text)
