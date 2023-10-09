import pygame, sys
from FacillimumLibrary import Facillimum_Library

class Main:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        self.screen_rect = self.screen.get_rect()

        self.FL = Facillimum_Library(self.screen)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run_game(self):
        while True:
            self.check_events()

if __name__ == "__main__":
    ai = Main()
    ai.run_game()