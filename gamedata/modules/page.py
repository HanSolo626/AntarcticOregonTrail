from button import *

class Page:
    """The parent class for all Pages."""
    def __init__(self, ai_game) -> None:

        # Gets screen object from thing that is importing it. (In this case 'main.py', which has a screen object.)
        self.screen = ai_game.screen
        
        self.button_list = []
        self.background = None


    def set_button_list(self, button_list: list[Button]):
        """Set the button list in list format."""

        self.button_list = button_list



    def draw_buttons(self):
        for button in self.button_list:
            button.draw_button(self.screen)