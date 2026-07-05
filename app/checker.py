import json
from app.zara import check_zara


def check():

    with open("products.json", "r", encoding="utf-8") as file:
        products = json.load(file)

    results = []

    for product in products:

        if product["site"] == "zara":

            results.append(check_zara(product))

    return results
