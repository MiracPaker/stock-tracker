import requests


def check_zara(product):

    url = (
        f"https://www.zara.com/itxrest/1/catalog/store/"
        f"{product['store']}/product/id/"
        f"{product['productId']}/availability"
    )

    response = requests.get(url, timeout=30)

    data = response.json()

    in_stock = False

    for sku in data["skusAvailability"]:

        if sku["availability"] != "out_of_stock":
            in_stock = True
            break

    return {
        "name": product["name"],
        "url": product["url"],
        "size": product["size"],
        "instock": in_stock
    }
