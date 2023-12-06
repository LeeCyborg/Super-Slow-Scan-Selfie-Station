#!usr/bin/env python  
#coding=utf-8  
import glob
import os
import pyaudio  
import wave  
import schedule
from PIL import Image
import time
from pysstv import color

chunk = 1024  
mode = color.Robot36
rate = 48000
bits = 16

def playNewPicture():
    makeWav()
    playSound()

def makeWav():
    files = glob.glob("*.png")
    files.sort(key=os.path.getmtime)
    myNewFile = files.pop()
    image = Image.open(myNewFile)
    s = mode(image, rate, bits)
    s.write_wav("rssstv.wav")
    print("made a new file")

def playSound():
    #open a wav format music  
    f = wave.open("rssstv.wav","rb")  
    #instantiate PyAudio  
    p = pyaudio.PyAudio()  
    #open stream  
    print("starting to play file")
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
    #read data  
    data = f.readframes(chunk)  
          #playStream
    while data:  
        stream.write(data)  
        data = f.readframes(chunk)  
    print("Done playing file")


schedule.every(5).seconds.do(playNewPicture)

while True:
    schedule.run_pending()
    time.sleep(1)