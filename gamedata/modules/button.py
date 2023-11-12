import pygame
from gamedata.modules.image_manager import *
from gamedata.modules.high_variable_manager import *

class Button:
    """The parent class for all buttons."""
    
    def __init__(self, function, x: int, y: int) -> None:
        
        self.action = None
        self.hover = None
        self.words = str
        self.letter_size = 0
        self.letter_color = (0, 0 ,0)
        self.image = None
        self.funtion = function

        self.x = x
        self.y = y


        
    def set_stats(self, action: VariableManager, words: str, image: pygame.Surface, letter_size: int, letter_color):
        """Set the image, letter size, and letter color of the button. letter_color must be (R,G,B) format. example for red: (255, 0, 0)"""

        self.action = action
        self.words = words
        self.image = image
        self.letter_size = letter_size
        self.letter_color = letter_color

        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.x
        self.image_rect.y = self.y

        # Create a font object to make words.
        self.font =  pygame.font.SysFont("", self.letter_size)

        # Render a Surface from the font object.
        self.word_image = self.font.render(self.words, True, self.letter_color)
        self.word_image_rect = self.word_image.get_rect()
        self.word_image_rect.center = self.image_rect.center


    def check_button(self, mouse_button_status):
        """Check if the button is being clicked and do whatever asignment it was given."""

        # If the mouse is hovering over the image rect...
        if self.image_rect.collidepoint(pygame.mouse.get_pos()):
            self.perform_hover_function()

            # If the mouse is clicked too...
            if mouse_button_status:
                self.perform_click_function()


    def perform_click_function(self):
        """Do the function when the button is being clicked on."""
        self.action(self)


    def perform_hover_function(self):
        """Do the function when the button is being hovered over."""

        print("ho!")


    def draw_button(self, screen):
        """Draw the button on the passed in screen."""
        screen.blit(self.image, self.image_rect)
        screen.blit(self.word_image, self.word_image_rect)
        



class TestButton(Button):
    def __init__(self, function, x: int, y: int) -> None:
        super().__init__(function, x, y)

        self.set_stats(function, "", Image("ArrowRight").return_image(), 0, (0,0,0))


class ExitGame(Button):
    def __init__(self, function, x: int, y: int) -> None:
        super().__init__(function, x, y)

        self.set_stats(function, "", Image("Exit").return_image(), 0, (0,0,0))

