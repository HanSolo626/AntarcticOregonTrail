import pygame
from gamedata.modules.image_manager import *
from gamedata.modules.high_variable_manager import *
from gamedata.modules.sound_manager import *

class Button:
    """The parent class for all buttons."""
    
    def __init__(self, function, x: int, y: int) -> None:
        
        self.action = None
        self.hover_image = None
        self.normal_image = None
        self.sound = None
        self.words = str
        self.letter_size = 0
        self.letter_color = (0, 0 ,0)
        self.current_image = None
        self.funtion = function

        self.x = x
        self.y = y

        self.sm = SoundManager()


        
    def set_stats(self, action: VariableManager, words: str, normal_image: pygame.Surface, hover_image: pygame.Surface, letter_size: int, letter_color, sound_effect: str):
        """
        Set the image, letter size, letter color, and sound of the button. letter_color must be (R,G,B) format. example for red: (255, 0, 0). \n
        NOTE: When setting hover_image, put in None if no hover current_image is desired.
        """

        self.action = action
        self.words = words
        self.hover_image = hover_image
        self.normal_image = normal_image
        self.letter_size = letter_size
        self.letter_color = letter_color
        self.sound = sound_effect

        self.image_rect = self.normal_image.get_rect()
        self.image_rect.x = self.x
        self.image_rect.y = self.y

        # Create a font object to make words.
        self.font =  pygame.font.SysFont("", self.letter_size)

        # Render a Surface from the font object.
        self.word_image = self.font.render(self.words, True, self.letter_color)
        self.word_image_rect = self.word_image.get_rect()
        self.word_image_rect.center = self.image_rect.center

        if hover_image == None:
            self.hover_image = self.normal_image


    def check_button(self, mouse_button_status):
        """Check if the button is being clicked and do whatever asignment it was given."""

        # Little peice of logic that ensures that button is only clicked once.
        if not mouse_button_status:
            self.click = True


        # If the mouse is hovering over the current_image rect...
        if self.image_rect.collidepoint(pygame.mouse.get_pos()):
            self.perform_hover_function()

            # Set current image to hover image
            self.current_image = self.hover_image
            self.image_rect = self.hover_image.get_rect()
            self.image_rect.x = self.x
            self.image_rect.y = self.y

            # If the mouse is clicked too...
            if mouse_button_status and self.click:
                self.perform_click_function()
                self.sm.play_effect(self.sound)
                self.click = False

        else:
            self.current_image = self.normal_image
            self.image_rect = self.normal_image.get_rect()
            self.image_rect.x = self.x
            self.image_rect.y = self.y


    def perform_click_function(self):
        """Do the function when the button is being clicked on."""
        self.action(self)


    def perform_hover_function(self):
        """Do the function when the button is being hovered over. (AKA, DO NOTHING)"""
        return None


    def draw_button(self, screen):
        """Draw the button on the passed in screen."""
        screen.blit(self.current_image, self.image_rect)
        screen.blit(self.word_image, self.word_image_rect)
        



class TestButton(Button):
    def __init__(self, function, x: int, y: int) -> None:
        super().__init__(function, x, y)

        self.set_stats(function, "yay", Image("ArrowRight").return_image(), None, 10, (255,0,0), "Z_Secret")


class ExitGame(Button):
    def __init__(self, function, x: int, y: int) -> None:
        super().__init__(function, x, y)

        self.set_stats(function, "", Image("Exit").return_image(), None, 0, (0,0,0), None)

