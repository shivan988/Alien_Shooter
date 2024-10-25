import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print(event.key)
            elif event.key == pygame.K_LEFT:
                print(event.key)
            elif event.key == pygame.K_UP:
                print(event.key)
            elif event.key == pygame.K_DOWN:
                print(event.key)

    screen.fill("blue")
    pygame.display.flip()

pygame.quit()


