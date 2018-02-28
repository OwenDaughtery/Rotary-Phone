import pygame
import time
import os


print( os.getcwd() )
pygame.mixer.init(frequency=44100,channels=2)

#file = open(file="Phone.wav",mode="rb")

mysound = pygame.mixer.Sound("Phone.wav")
time.sleep(1)
mysound.play()
time.sleep(10)