import os
import time
import pygame
import sys
import random
import gpiozero

import signal
terminate=False


def handler(signum, frame):
    global terminate
    print("Termination requested")
    terminate = True

signal.signal(signal.SIGTERM, handler)

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

pygame.init()
#pygame.display.set_mode((100, 100))
pygame.mixer.init(48000, -16, 2, 1024)
pygame.mixer.music.load("Phone.mp3")
#pygame.mixer.music.play()
#time.sleep(5)
#pygame.mixer.music.stop()

#Dictionary containing the file strings and the length of that audio file in seconds#

receiverInput = gpiozero.InputDevice(27, pull_up=True)
receiverOutput = gpiozero.OutputDevice(17, initial_value=False)

matInput = gpiozero.InputDevice(22, pull_up=True)
matOutput = gpiozero.OutputDevice(23, initial_value=False)
previouslyChosen = 0
audioFiles = [("only-2-socks.mp3", 12), ("struggle-different-culture.mp3", 30), ("using-PAs.mp3", 28)]
#audioObjects = [pygame.mixer.Sound(file) for file in audioFiles]

pygame.mixer.music.load("beep.mp3")
pygame.mixer.music.play()

def idle():

    while True:
        if(matInput.value and not receiverInput.value):
            phoneRing()
        if(terminate):
            matInput.close()
            matOutput.close()
            receiverInput.close()
            receiverOutput.close()
            exit()
        time.sleep(0.1)

def phoneRing():
    global previouslyChosen
    pygame.mixer.music.load("Phone.mp3")
    pygame.mixer.music.play()
    #rotaryRing.play()
    pickedUp = pickUpTimer(27, "Phone.mp3", receiverInput.value, True)
    if pickedUp:
        #Selecting audio file to play
        randomNum = random.randint(1,2)
        index = (randomNum+previouslyChosen)%len(audioFiles)
        previouslyChosen = randomNum

        #objectToPlay = audioObjects[randomNum]
        #objectToPlay.play()
        objectToPlay,audioLength = audioFiles[index]
        #audioLength = objectToPlay.get_length()
        pygame.mixer.music.load(objectToPlay)
        pygame.mixer.music.play()
        pickUpTimer(audioLength, objectToPlay, receiverInput.value, False)
        time.sleep(20)
    else: #Receiver wasn't picked up, time out whole program for 30 seconds
        #pygame.mixer.music.stop()
        time.sleep(20)

#pickUpTimer takes 3 parameters,
#1: How long the timer should last,
#2: Name of the file that should stop playing
#3: Whether the while loop should exit if the phone is "off the hook" or not,
#If the 3rd parameter is False the while loop will be ran as long as the phone hasn't been picked up.
def pickUpTimer(timerEnd, objectToPlay, offHook, triggerWhen):
    print("pickuptimer called")
    #pickedUp = False       
    timer = 0
    startTime = time.time()
    while timer<timerEnd and offHook != triggerWhen:
        if(receiverInput.value==triggerWhen):
            offHook = not offHook
                    
        timer = time.time() - startTime
        print(timer)
        time.sleep(0.01)
            
    print("leaving timer")
    pygame.mixer.music.stop()
    return offHook==triggerWhen
        
def receiverPickedUp():
    #Code for testing whether phone is off the hook

    return Boolean
        
idle()
