from pywebio.input import textarea, select, checkbox, radio, FLOAT, DATE, PASSWORD, DATETIME, input as input_pw, slider, \
    input_group
from pywebio.output import put_success, put_error, put_warning, put_image, put_html, put_table
from pywebio.session import run_js
from pywebio import start_server
import requests
from pprint import pprint

url = 'https://dummyjson.com/products'


def get_products() -> list[dict]:
    params = {'limit': 200}
    response = requests.get(url=url, params=params)
    response_json = response.json()
    products = response_json['products']
    return products


def get_products_total_cost(
        products: list[dict],
        min_price: float | int = 0,
        max_price: float | int = 50000,
        brand: str = None,
) -> float:
    total_cost = 0
    for product in products:
        product_price = product['price']
        product_stock = product['stock']

        if min_price <= product_price <= max_price:
            print(product)
            if brand and brand != product.get('brand'):
                continue
            total_cost += product_price * product_stock

    return round(total_cost, 2)


def main():
    products = get_products()
    total_cost = get_products_total_cost(products=products, min_price=999, max_price=7786, brand='ddd')


if __name__ == "__main__":
    main()
