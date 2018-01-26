#Dictionary containing the file strings and the length of that audio file in seconds
audioFiles = {0 : ("audio0.mp3", 15), 1 : ("audio1.mp3", 21), 2 : ("audio2.mp3", 17)}

def idle():
    while PresureMat not pressed:
        if presureMat pressed:
            phoneRing()

def phoneRing():
    play("phoneRing.mp3")
    timer = 0
    pickedUp = False
    startTime = time.time()
    while timer<30 and not pickedUp:
        pickedUp = receiverPickedUp
        timer = time.time() - startTime 
        time.sleep(0.01)
    stop("phoneRing.mp3")
    if pickedUp:
        #Selecting audio file to play
        randomNum = randint(0,3)
        fileToPlay,audioLength = audioFiles[randomNum]
        play(fileToPlay)
        timer = 0
        startTime = time.time()
        #While loop to test whether audio file runs out "organically" or is hung up on
        while timer<audioLength and pickedUp:
            timer = time.time() - startTime
            pickedUp = receiverPickedUp
            if not pickedUp:
                stop(fileToPlay)
            time.sleep(0.01)
        time.sleep(30)
    else: #Receiver wasn't picked up, time out whole program for 30 seconds
        time.sleep(30)

def receiverPickedUp():
    #Code for testing whether phone is off the hook
    return Boolean
        
idle()
