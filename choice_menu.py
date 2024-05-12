import keyboard


class ChoiceMenu:
    """
    A class to create and manage a keyboard-navigable choice menu.

    Attributes:
        choice_list (list[str]): A list of string choices for the menu.
        current_choice (int): The index of the currently selected choice.
    """

    choice_list: list[str]
    current_choice: int

    def __init__(self):
        """
        Initializes the choice menu allowing for use of class variables.

        Call create_menu() to initialize the choice menu.
        """

    def create_menu(self, choice_list: list[str]) -> int:
        """
        Displays the menu and sets up keyboard navigation keys.
        Blocks execution until the user confirms a choice with the enter key.

        Args:
            choice_list (list[str]): A list of choices for the menu.

        Returns:
            int: The index of the selected choice after the user presses enter.
        """
        self.choice_list: list[str] = choice_list
        self.truncate_menu()
        self.current_choice: int = 0

        keyboard.add_hotkey('left', self._previous)
        keyboard.add_hotkey('right', self._next)
        self._show_menu()
        keyboard.wait('enter')
        cleanup_keyboard_usage()
        return self.current_choice

    def truncate_menu(self):
        max_length = 20

        new_choice_list: list[str] = []
        for choice in self.choice_list:
            if len(choice) > max_length:
                choice = choice[:max_length] + '..'
            new_choice_list.append(choice)

        self.choice_list = new_choice_list

    def _previous(self) -> None:
        if self.current_choice == 0:
            # Wrap around selection
            self.current_choice = len(self.choice_list)
        self.current_choice -= 1
        self._show_menu()

    def _next(self) -> None:
        self.current_choice += 1
        if self.current_choice == len(self.choice_list):
            # Wrap around selection
            self.current_choice = 0
        self._show_menu()

    def _show_menu(self) -> None:
        """
        Renders the menu in the console, highlighting the current choice.
        """
        menu_string: str = ''
        for index, choice in enumerate(self.choice_list):
            if index == self.current_choice:
                menu_string += f' >{choice}< '
            else:
                menu_string += f'  {choice}  '

        print('\r' + menu_string, end='')


def cleanup_keyboard_usage():
    keyboard.unhook_all()  # Zorgt ervoor dat er niet meer geluisterd wordt naar keyboard input.
    print()  # add a blank line to make the choice menu stand out


if __name__ == '__main__':
    ChoiceMenu()
