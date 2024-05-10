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

    def create_menu(self, choice_list: list[str]) -> str:
        """
        Displays the menu and sets up keyboard navigation keys.
        Blocks execution until the user confirms a choice with the enter key.

        Args:
            choice_list (list[str]): A list of choices for the menu.

        Returns:
            str: The selected choice after the user presses enter.
        """
        self.choice_list: list[str] = choice_list
        self.current_choice: int = 0

        self._show_menu()
        keyboard.add_hotkey('left', self._previous)
        keyboard.add_hotkey('right', self._next)
        keyboard.wait('enter')
        print()
        return self.choice_list[self.current_choice]

    def _previous(self) -> None:
        if self.current_choice == 0:
            self.current_choice = len(self.choice_list)
        self.current_choice -= 1
        self._show_menu()

    def _next(self) -> None:
        self.current_choice += 1
        if self.current_choice == len(self.choice_list):
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
