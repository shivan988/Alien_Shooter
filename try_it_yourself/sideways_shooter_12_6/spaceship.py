import pygame


class SpaceShip:
    def __init__(self, rocket_game):
        self.screen = rocket_game.screen
        self.screen_rect = self.screen.get_rect()

        # loading rocket image and its rectangle
        self.image = pygame.image.load("rocket (1).bmp")
        self.rect = self.image.get_rect()

        # setting it on the screen
        self.rect.bottomleft = self.screen_rect.bottomleft

        # movement flag
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update(self):
        # if self.move_right and self.rect.right < self.screen_rect.right:
            # self.rect.x += 1
        # if self.move_left and self.rect.left > self.screen_rect.left:
        #     self.rect.x -= 1
        if self.move_down and self.rect.y < 650:
            self.rect.y += 1
        if self.move_up and self.rect.y > 0:
            self.rect.y -= 1



    def blitme(self):
        self.screen.blit(self.image, self.rect)


