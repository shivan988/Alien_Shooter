import pygame
import sys
from rocket import Rocket


class RocketGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("The rocket game".title())

        self.rocket = Rocket(self)

    def run_game(self):
        while True:
            self._check_event()
            self.update_screen()
            self.rocket.update()
    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.move_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.move_left = True
        elif event.key == pygame.K_UP:
            self.rocket.move_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.move_down = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.move_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.move_left = False
        elif event.key == pygame.K_UP:
            self.rocket.move_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.move_down = False

    def update_screen(self):
        self.screen.fill((240, 240, 240))
        self.rocket.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    rg = RocketGame()
    rg.run_game()






