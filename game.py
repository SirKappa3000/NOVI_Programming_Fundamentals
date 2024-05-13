import json
import requests
import random
from choice_menu import ChoiceMenu


class Product:
    def __init__(self, id, title, price, category, description, image):
        """
        Initializes a Product instance with detailed attributes about the product.

        Parameters:
        - id (int): Unique identifier for the product.
        - title (str): Name of the product.
        - price (float): Price of the product.
        - category (str): Category the product belongs to.
        - description (str): Description of the product.
        - image (str): URL to the product's image.
        """
        self.id: int = id
        self.title: str = title
        self.price: float = price
        self.category: str = category
        self.description: str = description
        self.image: str = image


class Highscore:
    """
    Initializes a Highscore instance with player name and score.

    Parameters:
    - name (str): The player's name.
    - score (float): The score achieved by the player.
    """
    def __init__(self, name: str, score: float):
        self.name: str = name
        self.score: float = score


class ShoppingGame:
    def __init__(self):
        """
        Initializes a ShoppingGame instance with game settings.
        """
        self.countdown: int = 60
        self.time_per_choice: int = 10
        self.score: int = 0
        self.choice_menu_factory: ChoiceMenu = ChoiceMenu()

    def start_new_game(self, player_name: str) -> None:
        """
        Starts a new game session, managing the game time and product selections.
        """
        print("Good luck and have fun!", end="\n\n")
        self.countdown = 30
        self.score = 0

        # main game loop
        while self.countdown > 0:
            print(f'You have {self.countdown} seconds left.')
            chosen_category: str = self.choose_category()
            chosen_product: Product = self.choose_product(chosen_category)
            print(f'You chose {chosen_product.title}')
            print(f'It costs €{chosen_product.price:.2f}')

            # finalize round variables
            self.score += chosen_product.price
            self.countdown -= self.time_per_choice

        print("Time's up!")
        print(f"Your final scoring is €{self.score:.2f}.")
        add_highscore(player_name, self.score)

        return

    def choose_category(self) -> str:
        """
        Displays a menu of categories and allows the player to choose one.

        Returns:
        - (str): The chosen category.
        """
        category_list: list[str] = get_random_categories()
        print('Choose a category')
        choice_index: int = self.choice_menu_factory.create_menu(category_list)
        return category_list[choice_index]

    def choose_product(self, category: str) -> Product:
        """
        Displays a menu of products from the chosen category and allows the player to select one.

        Parameters:
        - category (str): The chosen category from which to display products.

        Returns:
        - Product: The chosen product object.
        """
        product_list: list[Product] = get_random_products_in_category(category)
        product_name_list: list[str] = [product.title for product in product_list]
        print('Choose a product')
        choice_index: int = self.choice_menu_factory.create_menu(product_name_list)
        return product_list[choice_index]


# Static function, does not need to be in class to be called.
# private function, not recommended for use outside of this file.
def _get(endpoint: str, params: dict = None) -> requests.Response:
    """
    Performs a GET request to the specified API endpoint.

    Parameters:
    - endpoint (str): The API endpoint to hit.
    - params (dict): Optional parameters to be sent with the request.

    Returns:
    - requests.Response: The response object from the requests library.
    """
    try:
        return requests.get('https://fakestoreapi.com/products/' + endpoint, params=params)
    except requests.exceptions.ConnectionError:
        print('Connection error')


# Static function, does not need to be in class to be called.
def get_random_categories() -> list[str]:
    """
    Fetches a random set of product categories from the API.

    Returns:
    - list[str]: A list of 3 random product categories.
    """
    try:
        categories: list[str] = _get('categories').json()
        return random.sample(categories, 3)  # get 3 random items from the list
    except json.decoder.JSONDecodeError:
        print('invalid response from the server. Try again later.')


# Static function, does not need to be in class to be called.
def get_random_products_in_category(category: str) -> list[Product]:
    """
    Fetches a list of products within a specified category from the API.

    Parameters:
    - category (str): The product category to fetch products from.

    Returns:
    - list[Product]: A list of 3 random products from the specified category.
    """
    try:
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


def get_highscores() -> list[Highscore]:
    """
    Reads and returns high scores from a local JSON file.

    Returns:
    - list[Highscore]: A list of high score records.
    """
    with open('highscores.json') as higscores_file:
        highscores: list[Highscore] = []
        for score_dict in json.load(higscores_file):
            highscores.append(Highscore(score_dict['name'], score_dict['score']))

        return highscores


def add_highscore(name: str, highscore: int) -> None:
    """
    Adds a new high score entry to the local JSON file and saves it.

    Parameters:
    - name (str): The player's name.
    - highscore (int): The score to add.
    """
    with open('highscores.json', mode='r') as highscores_file:
        highscores_json = json.load(highscores_file)
        highscores_json.append({'name': name, 'score': highscore})

        with open('highscores.json', 'w') as highscores_file_writable:
            highscores_file_writable.write(json.dumps(highscores_json))


if __name__ == '__main__':
    ShoppingGame().start_new_game()
