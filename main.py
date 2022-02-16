import serial
import os
import pyttsx3
import data_retriever

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

ard = serial.Serial('COM3',timeout=1)
print(ard)
while True:
    if ard.readline != None:
        speak(data_retriever.weather())
        speak(data_retriever.actus())
        os.startfile("build\\exe.win-amd64-3.8\\voice_commands.exe")
        os.startfile("C:\\Programmes\\Microsoft VS Code\\Code.exe")
        break 
    else:
        print(str(ard.readline().decode('UTF-8')))
