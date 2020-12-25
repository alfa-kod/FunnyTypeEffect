from pynput.keyboard import Key, Listener
import pygame
from pygame.locals import *
import os
cwd = os.getcwd()
pygame.init()

lastkey = ""#Save the last key for exit proccess
lastpressed = ""
def on_press(key):
    global lastpressed
    #When pressed a key play sound with pygame
    soundDirClick = cwd + "\\sounds\\click.mp3"
    soundDirClick = soundDirClick.replace("\\", "/")

    soundDirEnter = cwd + "\\sounds\\enter.mp3"
    soundDirEnter = soundDirEnter.replace("\\", "/")

    soundDirBackspace = cwd + "\\sounds\\backspace.mp3"
    soundDirBackspace = soundDirBackspace.replace("\\", "/")

    soundDirSpace = cwd + "\\sounds\\space.mp3"
    soundDirSpace = soundDirSpace.replace("\\", "/")

    soundDirDelete = cwd + "\\sounds\\delete.mp3"
    soundDirDelete = soundDirSpace.replace("\\", "/")
    
    if key == Key.enter:
        sound = pygame.mixer.Sound(soundDirEnter)
    elif key == Key.backspace:
        sound = pygame.mixer.Sound(soundDirBackspace)
    elif key == Key.space:
        sound = pygame.mixer.Sound(soundDirSpace)
    elif key == Key.delete:
        sound = pygame.mixer.Sound(soundDirDelete)
    else:
         sound = pygame.mixer.Sound(soundDirClick)
    
    if lastpressed != key:
        sound.play()
    lastpressed = key

def on_release(key):
    global lastkey
    global lastpressed
    #If pressed F4   
    if key == Key.f4:
        #If pressed Esc before F4 
        if lastkey==Key.esc:
            return False#exit the program
    lastkey = key
    lastpressed = ""
# Collect events until released
print("If you want to exit press Esc and F4 on this screen")
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
