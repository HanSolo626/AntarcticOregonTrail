import pygame

from gamedata.modules.image_manager import *

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



        
    def set_stats(self, action, words: str, normal_image: pygame.Surface, hover_image: pygame.Surface, letter_size: int, letter_color, sound_effect: str):
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

        self.current_image = self.hover_image


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
                if self.sound != None:
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
        #if self.action:
        #    print("g")
        #else:
        #    self.action(self) #NOTE BUG


    def perform_hover_function(self):
        """Do the function when the button is being hovered over. (AKA, DO NOTHING)"""
        return None


    def draw_button(self, screen):
        """Draw the button on the passed in screen."""
        screen.blit(self.current_image, self.image_rect)
        screen.blit(self.word_image, self.word_image_rect)




class TextField:
    """The parent class for text fields, used to display just text."""
    def __init__(self, text: str, x: int, y: int) -> None:
        
        self.text = text
        self.x = x
        self.y = y
        self.moving_text = None

        self.text_number = 0
        self.text_length = self.text.__len__()
        self.currently_displayed_text = ""
        self.sound_played = False

        self.sm = SoundManager()


    def set_stats(self, letter_size: int, letter_color, sound_effect: str, moving_text: bool):
        """Set the the font size, the letter color, and the sound effect name, to be played when the text is displayed."""

        self.letter_size = letter_size
        self.letter_color = letter_color
        self.sound_effect = sound_effect
        self.moving_text = moving_text

        self.font =  pygame.font.SysFont("", self.letter_size)

        if not self.moving_text:
            self.sound_played = True
            self.text_number = self.text_length
            self.currently_displayed_text = self.text


    def draw_button(self, screen):
        """Draw the text field while updating the text span."""

        
        word_image = self.font.render(self.currently_displayed_text, True, self.letter_color)
        word_image_rect = word_image.get_rect()
        word_image_rect.x = self.x
        word_image_rect.y = self.y
        screen.blit(word_image, word_image_rect)

        
        if not self.text_number == self.text_length:
            self.currently_displayed_text += self.text[self.text_number]
            self.text_number += 1

        if self.sound_played == False:
            self.sm.play_effect(self.sound_effect)
            self.sound_played = True

    def check_button(self, mouse_pos):
        return None




















class SimpleField(TextField):
    def __init__(self, text: str, x: int, y: int) -> None:
        super().__init__(text, x, y)

        self.set_stats(40, (255, 255, 255), "Z_Secret", False)


class BasicText(TextField):
    def __init__(self, text: str, x: int, y: int) -> None:
        super().__init__(text, x, y)

        self.set_stats(40, (255,255,255), "Z_Secret", True)



class TestButton(Button):
    def __init__(self, function, x: int, y: int) -> None:
        super().__init__(function, x, y)

        self.set_stats(function, "yay", Image("ArrowRight").return_image(), None, 50, (255,0,0), "Z_Secret")




class ExitGame(Button):
    def __init__(self, function, x: int, y: int) -> None:
        super().__init__(function, x, y)


        self.set_stats(function, "", Image("Exit").return_image(), None, 0, (0,0,0), None)

class HomeOptions(Button):
    def __init__(self, function, x: int, y: int) -> None:
        super().__init__(function, x, y)


        self.set_stats(function, "", Image("Options").return_image(), Image("OptionsHover").return_image(), 0, (0,0,0), "ButtonClicked")

class NextButton(Button):
    def __init__(self, function, x: int, y: int) -> None:
        super().__init__(function, x, y)

        self.set_stats(function, "", Image("Next").return_image(), Image("NextHover").return_image(), 0, (0,0,0), "ButtonClicked")
