import time
from choice_menu import ChoiceMenu
import requests


def main():
    # welcome_window()
    # if input('Would you like some instructions? (y/N) ').strip().lower() == 'y':
    #     show_instructions()

    menu_class: ChoiceMenu = ChoiceMenu()  # Create a choice menu class

    print('Start or Stop the game now?')
    if menu_class.create_menu(['Start', 'Stop']) == 1:
        print('Bye now!')
    else:
        choices = ['choice 1', 'choice 2', 'choice 3']
        for choice in choices:
            choice_index: int = menu_class.create_menu(choices)
            choice: str = choices[choice_index]
            print(f'You chose {choice}', end='\n\n')


def welcome_window() -> None:
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
