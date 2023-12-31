from gamedata.modules.button import *
from gamedata.modules.image_manager import *

class Page:
    """The parent class for all Pages."""
    def __init__(self, ai_game) -> None:

        # Gets screen object from thing that is importing it. (In this case 'main.py', which has a screen object.)
        self.screen = ai_game.screen
        
        self.button_list = []
        self.background = None
        self.background_rect = None


    def set_button_list(self, button_list: list):
        """Set the button list in list format."""

        self.button_list = button_list

    def draw_self(self):
        self.screen.blit(self.background, self.background_rect)
        self.draw_buttons()

    def draw_buttons(self):
        for button in self.button_list:
            button.draw_button(self.screen)

    def set_background(self, image: Image):
        """Set the image for the page background."""
        self.background = image
        self.background_rect = image.get_rect()





class TestPage(Page):
    def __init__(self, ai_game) -> None:
        super().__init__(ai_game)

        self.set_background(Image("Test Background").return_image())

        self.set_button_list([
            TestButton(1600, 600)
        ]
            )