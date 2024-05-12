import json

import requests
import random
from choice_menu import ChoiceMenu


class Product:
    def __init__(self, id, title, price, category, description, image):
        self.id: int = id
        self.title: str = title
        self.price: float = price
        self.category: str = category
        self.description: str = description
        self.image: str = image


# Static function, does not need to be in class to be called.
def _get(endpoint: str, params: dict = None) -> requests.Response:
    try:
        return requests.get('https://fakestoreapi.com/products/' + endpoint, params=params)
    except requests.exceptions.ConnectionError:
        print('Connection error')


class ShoppingGame:
    def __init__(self):
        self.countdown: int = 60
        self.time_per_action: int = 5
        self.choice_menu_factory: ChoiceMenu = ChoiceMenu()

    def start_new_game(self) -> None:
        self.countdown: int = 60
        while self.countdown > 0:
            print(f'You have {self.countdown} seconds left.')
            chosen_category: str = self.choose_category()
            chosen_product: Product = self.choose_product(chosen_category)
            print(f'You chose {chosen_product.title}')
            print(f'It costs €{chosen_product.price}')

        print("Time's up!")
        return

    def choose_category(self) -> str:
        category_list: list[str] = self.get_random_categories()
        choice_index: int = self.choice_menu_factory.create_menu(category_list)
        return category_list[choice_index]

    def choose_product(self, category: str) -> Product:
        product_list: list[Product] = self.get_random_products_in_category(category)
        product_name_list: list[str] = [product.title for product in product_list]

        choice_index: int = self.choice_menu_factory.create_menu(product_name_list)
        return product_list[choice_index]

    def get_random_categories(self) -> list[str]:
        try:
            self.countdown -= self.time_per_action
            categories: list[str] = _get('categories').json()
            return random.sample(categories, 3)  # get 3 random items from the list
        except json.decoder.JSONDecodeError:
            print('invalid response from the server. Try again later.')

    def get_random_products_in_category(self, category: str) -> list[Product]:
        try:
            self.countdown -= self.time_per_action
            response_dicts: list[{}] = _get(f'category/{category}').json()
            products: list[Product] = [
                Product(a_product['id'],
                        a_product['title'],
                        a_product['price'],
                        a_product['category'],
                        a_product['description'],
                        a_product['image'],
                        ) for a_product in response_dicts]
            return random.sample(products, 3)
        except json.decoder.JSONDecodeError:
            print('Invalid category')


if __name__ == '__main__':
    ShoppingGame()