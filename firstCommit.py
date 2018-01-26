#Dictionary containing the file strings and the length of that audio file in seconds
audioFiles = {0 : ("audio0.mp3", 15), 1 : ("audio1.mp3", 21), 2 : ("audio2.mp3", 17)}

def idle():
    while PresureMat not pressed:
        if presureMat pressed:
            phoneRing()

def phoneRing():
    play("phoneRing.mp3")
    pickedUp = pickUpTimer(30, "phoneRing.mp3", False)
    if pickedUp:
        #Selecting audio file to play
        randomNum = randint(0,3)
        fileToPlay,audioLength = audioFiles[randomNum]
        play(fileToPlay)
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
    pickedUp = ReceiverPickedUp()        
    timer = 0
    startTime = time.time()
    while timer<timerEnd and pickedUp == offHook:
        pickedUp = receiverPickedUp()
        timer = time.time() - startTime 
        time.sleep(0.01)
        if not offHook:
            stop(fileName) 
    return timer<timerEnd
        
def receiverPickedUp():
    #Code for testing whether phone is off the hook
    return Boolean
        
idle()
