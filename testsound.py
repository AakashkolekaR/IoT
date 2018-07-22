from pygame import *

def playsound(song):
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()
    while mixer.music.get_busy():
        time.Clock().tick(2)
