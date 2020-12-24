from pynput.keyboard import Key, Listener
import pygame
from pygame.locals import *

pygame.init()

lastkey = ""#Save the last key for exit proccess
lastpressed = ""
def on_press(key):
    global lastpressed
    #When pressed a key play sound with pygame
    sound = pygame.mixer.Sound("click.mp3")
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