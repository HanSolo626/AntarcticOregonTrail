import pygame, sys


from FacillimumLibraryOregon import Facillimum_Library
from gamedata.modules.page import *

class Main:
    def __init__(self) -> None:

        pygame.init()

        self.screen = pygame.display.set_mode((2000, 1200), pygame.SCALED | pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()

        self.FL = Facillimum_Library(self.screen)

        # Test page
        self.current_page = TestPage(self)

        # Mouse button status
        self.left_click = False
        self.right_click = False






    def check_events(self):
        for event in pygame.event.get():

            # Check for quit
            if event.type == pygame.QUIT:
                sys.exit()


            # Check for mouse clicks
            elif event.type == pygame.MOUSEBUTTONUP:
                self.recorded_lod = True
                if not pygame.mouse.get_pressed()[0]:
                    self.left_click = False
                if not pygame.mouse.get_pressed()[2]:
                    self.right_click = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    self.left_click = True
                if pygame.mouse.get_pressed()[2]:
                    self.right_click = True



    def check_current_page(self):
        """Check the current page."""
        self.current_page.check_buttons(self.left_click)








    def run_game(self):
        """Start the game loop."""
        while True:

            # Check everything
            self.check_events()
            self.check_current_page()


            # Update and draw everything
            self.current_page.draw_self()
            self.FL.update()


if __name__ == "__main__":
    ai = Main()
    ai.run_game()