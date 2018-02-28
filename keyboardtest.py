import pygame
import sys
pygame.init()

pygame.display.set_mode((100, 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print('Forward')
            elif event.key == pygame.K_s:
                print('Backward')