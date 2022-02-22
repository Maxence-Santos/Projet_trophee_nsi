import serial
import os
import pyttsx3
import data_retriever
import time
import psutil
import subprocess
import wmi

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def trouverInstance():
    f = wmi.WMI()
    pr = []
    for process in f.Win32_Process():
        pr.append(process.name)
    if "Code.exe" not in pr:
        os.startfile("C:\\Program Files\\Microsoft VS Code\\Code.exe")


ard = serial.Serial('COM3', timeout=1)
print(ard)

while True:
    # print(ard.readline())
    # if str(ard.readline().decode('UTF-8')) != "" :
    if ard.readline() == b'D\xc3\xa9tect\xc3\xa9\r\n':
        trouverInstance()
        speak(data_retriever.weather())
        speak(data_retriever.actus())
        time.sleep(2)
        os.startfile("build\\exe.win-amd64-3.8\\voice_commands.exe")
    elif ard.readline() == b'Low\r\n':
        name1 = 'voice_commands.exe'
        f = wmi.WMI()
        pr = []
        for process in f.Win32_Process():
            if process.name == name1:
                process.Terminate()
