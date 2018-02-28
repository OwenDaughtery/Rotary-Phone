import keyboard #Using module keyboard
import time
import pygame
import sys
import random
pygame.init()
pygame.display.set_mode((100, 100))
pygame.mixer.init()
pygame.mixer.music.load("Phone.mp3")
#pygame.mixer.music.play()
#time.sleep(5)
#pygame.mixer.music.stop()

#Dictionary containing the file strings and the length of that audio file in seconds#

audioFiles = [("only-2-socks.mp3", 11), ("struggle-different-culture.mp3", 29), ("using-PAs.mp3", 27)]
#audioObjects = [pygame.mixer.Sound(file) for file in audioFiles]

def idle():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    print("pressed")
                    phoneRing()

def phoneRing():
    pygame.mixer.music.load("Phone.mp3")
    pygame.mixer.music.play()
    #rotaryRing.play()
    pickedUp = pickUpTimer(27, "Phone.mp3", False, False)
    if pickedUp:
        print("entering random num")
        #Selecting audio file to play
        randomNum = random.randint(0,2)
        #objectToPlay = audioObjects[randomNum]
        #objectToPlay.play()
        objectToPlay,audioLength = audioFiles[randomNum]
        #audioLength = objectToPlay.get_length()
        pygame.mixer.music.load(objectToPlay)
        pygame.mixer.music.play()
        pickUpTimer(audioLength, objectToPlay, True, True)
        time.sleep(5)
        print("reset")
    else: #Receiver wasn't picked up, time out whole program for 30 seconds
        print("stopped due to not being picked up")
        #pygame.mixer.music.stop()
        time.sleep(5)
        print("reset")

#pickUpTimer takes 3 parameters,
#1: How long the timer should last,
#2: Name of the file that should stop playing
#3: Whether the while loop should exit if the phone is "off the hook" or not,
#If the 3rd parameter is False the while loop will be ran as long as the phone hasn't been picked up.
def pickUpTimer(timerEnd, objectToPlay, offHook, pickedUp):
    print("pickuptimer called")
    #pickedUp = False       
    timer = 0
    startTime = time.time()
    while timer<timerEnd and pickedUp == offHook:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    print("s pressed")
                    pickedUp = not pickedUp
                    
        timer = time.time() - startTime
        print(timer)
        time.sleep(0.01)
            
    print("leaving timer")
    pygame.mixer.music.stop()
    return pickedUp != offHook
        
def receiverPickedUp():
    #Code for testing whether phone is off the hook
    return Boolean
        
idle()
