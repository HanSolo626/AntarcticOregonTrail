import pygame, sys
from FacillimumLibrary import Facillimum_Library

class Main:
    def __init__(self) -> None:

        pygame.init()

        self.screen = pygame.display.set_mode((2000, 1200), pygame.SCALED | pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()

        self.FL = Facillimum_Library(self.screen)


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    def run_game(self):
        print(pygame.display.get_desktop_sizes())
        print(pygame.display.list_modes())
        #sys.exit()
        while True:
            self.check_events()
            self.FL.paint_screen("white")
            self.FL.draw_words("Command Q to quit.", 50, (50, 50), False, "black")
            self.FL.update()

if __name__ == "__main__":
    ai = Main()
    ai.run_game()