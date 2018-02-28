import pygame
import time
#pygame.init()

#gameDisplay = pygame.display.set_mode((640, 480))

pygame.mixer.init()
pygame.mixer.music.load("Phone.mp3")
pygame.mixer.music.play()
time.sleep(5)
pygame.mixer.music.stop()