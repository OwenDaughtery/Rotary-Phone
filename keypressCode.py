import keyboard #Using module keyboard
import pygame
#Dictionary containing the file strings and the length of that audio file in seconds
audioFiles = {0 : ("audio0.mp3", 15), 1 : ("audio1.mp3", 21), 2 : ("audio2.mp3", 17)}

def idle():

    while True:#making a loop
        try: #used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('a'): #if key 'a' is pressed 
                phoneRing()
            else:
                pass
        except:
            break #if user pressed other than the given key the loop will break

def phoneRing():
    pygame.mixer.init()
    pygame.mixer.music.load("ringing.mp3")
    pygame.mixer.music.play()
    pickedUp = pickUpTimer(30, "phoneRing.mp3", False)
    if pickedUp:
        #Selecting audio file to play
        randomNum = randint(0,3)
        fileToPlay,audioLength = audioFiles[randomNum]

        pygame.mixer.init()
        pygame.mixer.music.load(fileToPlay)
        pygame.mixer.music.play()
        pickUpTimer(audioLength, fileToPlay, True)
        time.sleep(30)
    else: #Receiver wasn't picked up, time out whole program for 30 seconds
        time.sleep(30)

#pickUpTimer takes 3 parameters,
#1: How long the timer should last,
#2: Name of the file that should stop playing
#3: Whether the while loop should exit if the phone is "off the hook" or not,
#If the 3rd parameter is False the while loop will be ran as long as the phone hasn't been picked up.
def pickUpTimer(timerEnd, fileName, offHook):        
    pickedUp = False       
    timer = 0
    startTime = time.time()
    while timer<timerEnd and pickedUp == offHook:
        try: #used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('b'): #if key 'a' is pressed 
                pickedUp = True
            else:
                pass
        except:
            break #if user pressed other than the given key the loop will break
        timer = time.time() - startTime 
        time.sleep(0.01)
        if not offHook:
            stop(fileName) #<--------------
    return timer<timerEnd
        
def receiverPickedUp():
    #Code for testing whether phone is off the hook
    return Boolean
        
idle()
