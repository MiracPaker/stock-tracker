from app.checker import check
from app.notifier import send

results = check()

for item in results:

    if item["instock"]:

        send(
            f"""🟢 STOĞA GİRDİ

{item["name"]}

Beden: {item["size"]}

{item["url"]}"""
        )
