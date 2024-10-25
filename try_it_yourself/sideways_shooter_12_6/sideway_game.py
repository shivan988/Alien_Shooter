"""Sideways Shooter: Write a game that places a ship on the left side of the 
screen and allows the player to move the ship up and down. Make the ship fire 
a bullet that travels right across the screen when the player presses the space
bar. Make sure bullets are deleted once they disappear off the screen.
"""

import pygame
import sys
from spaceship import SpaceShip
from bullets_spaceship import Bullet
from settings import Settings


class RocketGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("The rocket game".title())

        self.spaceship = SpaceShip(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_event()
            self.update_screen()
            self.spaceship.update()
            self._update_bullets()

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
            self.spaceship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.spaceship.move_left = True
        elif event.key == pygame.K_UP:
            self.spaceship.move_up = True
        elif event.key == pygame.K_DOWN:
            self.spaceship.move_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.spaceship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.spaceship.move_left = False
        elif event.key == pygame.K_UP:
            self.spaceship.move_up = False
        elif event.key == pygame.K_DOWN:
            self.spaceship.move_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= 1200:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

    def update_screen(self):
        self.screen.fill((240, 240, 240))
        self.spaceship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == "__main__":
    ssg = RocketGame()
    ssg.run_game()







        





