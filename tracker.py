from app.notifier import send
from app.checker import check

print("Stock Tracker başladı")

if check():
    send("🚀 Stock Tracker başarıyla çalışıyor.")
