import sys
import time
from choice_menu import ChoiceMenu
from game import ShoppingGame, Highscore, get_highscores, add_highscore


def main():
    # show_welcome_text()
    # if input('Would you like some instructions? (y/N) ').strip().lower() == 'y':
    #     show_instructions()

    menu_factory: ChoiceMenu = ChoiceMenu()  # Create a choice menu class
    game = ShoppingGame()  # Create a shopping game class

    print('Would you like to start a new game?')
    while menu_factory.create_menu(['Yes', 'No']) != 1:

        game.start_new_game()

        print('Would you like to play again?')

    print('Do you want to look at the current highscores?')
    if menu_factory.create_menu(['Yes', 'No']) == 0:
        highscore_list: list[Highscore] = get_highscores()
        print('{:<12} {:<8}'.format('NAME', 'SCORE'))
        for highscore in highscore_list:
            print(f'{highscore.name:<12} {highscore.score:<8}')
        print()

    print('Thank you for playing!\nGoobye!')


def show_welcome_text() -> None:
    print_multiple_lines([
        'Welcome to Totally Accurate Shopping Simulator (winkel-TASS)!',
        'You are going on a shopping spree with limited time.',
        'Your objective: get the highest value products in your cart.',
        'Good luck!'
    ])
    return


def show_instructions():
    print_multiple_lines([
        'This game is all about making the right choices.',
        'When you get a selection of choices, use the left and right arrow keys to navigate.',
        'Use enter to select an option.'
    ])
    return


def print_multiple_lines(lines_of_text: list[str], reading_time: float = 1.3) -> None:
    print()  # add a blank line so the textblock stands out
    for text in lines_of_text:
        print(text)
        time.sleep(reading_time)
    print()  # add a blank line to


if __name__ == '__main__':
    main()
    # test()
