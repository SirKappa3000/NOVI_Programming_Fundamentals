import requests

type Product = {
    'id': int,
    'title': str,
    'price': float,
    'category': str,
    'description': str,
    'image': str,
}


def start_new_game() -> None:
    print(get_categories())
    for category in get_categories():
        print(get_products_in_category(category))
    return


def get_categories() -> list[str]:
    response: requests.Response = requests.get('https://fakestoreapi.com/products/categories')
    return response.json()


def get_products_in_category(category: str) -> Product:
    response: requests.Response = requests.get(f'https://fakestoreapi.com/products/category/{category}')
    return response.json()


if __name__ == '__main__':
    start_new_game()
