import pygame
import sys
from game_charecter_12_2 import Character


class BlueSky:
    def __init__(self):
        pygame.init()
        self.bg_color = (235, 241, 255)
        self.screen = pygame.display.set_mode((1200, 500))
        self.character = Character(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.character.blitme()
            pygame.display.flip()


if __name__ == "__main__":
    bs = BlueSky()
    bs.run_game()
