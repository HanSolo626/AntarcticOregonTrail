import pygame
from gamedata.modules.image_manager import *

class Button:
    """The parent class for all buttons."""
    
    def __init__(self, function) -> None:
        
        self.words = str
        self.letter_size = 0
        self.letter_color = (0, 0 ,0)
        self.image = None
        self.funtion = function

        self.x = int
        self.y = int


        
    def set_stats(self, words: str, image: pygame.Surface, letter_size: int, letter_color, x: int, y: int):
        """Set the image, letter size, and letter color of the button. letter_color must be (R,G,B) format. example for red: (255, 0, 0)"""

        self.words = words
        self.image = image
        self.letter_size = letter_size
        self.letter_color = letter_color
        self.x = x
        self.y = y

        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.x
        self.image_rect.y = self.y

        # Create a font object to make words.
        self.font =  pygame.font.SysFont("", self.letter_size)

        # Render a Surface from the font object.
        self.word_image = self.font.render(self.words, True, self.letter_color)
        self.word_image_rect = self.word_image.get_rect()
        self.word_image_rect.center = self.image_rect


    def check_button(self, mouse_pos):
        """Check if the button is being clicked and do whatever asignment it was given."""

        # If the mouse is hovering over the image rect...
        if self.image_rect.collidepoint(mouse_pos):
            print("ha")


    def draw_button(self, screen):
        """Draw the button on the passed in screen."""
        screen.blit(self.image, self.image_rect)
        screen.blit(self.word_image, self.word_image_rect)
        



class TestButton(Button):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()

        self.set_stats("", Image("ArrowRight"), 0, (0,0,0), x, y)