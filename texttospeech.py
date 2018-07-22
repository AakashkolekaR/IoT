from gtts import gTTS
import pyglet
import time,os
from testsound import *


#text='Lights have been switched on '
#lang='en'


def tts(text,lang):
    mixer.init()
    file=gTTS(text=text,lang=lang)
    print("hi")
    filename='C:/Users/Aakash/PycharmProjects/classes/sound.mp3'
    #filename='/temp/tmp.mp3'
    file.save(filename)
    '''mus=pyglet.media.load(filename,streaming=False)
    mus.play()
    time.sleep(music.duration)
    os.remove(filename)'''
    playsound('sound.mp3')

#tts(text,lang)
