import serial
import os
import pyttsx3
import data_retriever
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

ard = serial.Serial('COM3',timeout=1)
print(ard)

while True:
    #print(type(str(ard.readline().decode('UTF-8'))))
    if str(ard.readline().decode('UTF-8')) != "" : 
        os.startfile("C:\\Program Files\\Microsoft VS Code\\Code.exe")
        speak(data_retriever.weather())
        speak(data_retriever.actus())
        time.sleep(2)
        os.startfile("build\\exe.win-amd64-3.8\\voice_commands.exe") 