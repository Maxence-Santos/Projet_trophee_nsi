##### IMPORT DES LIBRAIRIES ######

import serial
import os
import pyttsx3
import wmi
import voice_commands

###### -  ######

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
ard = serial.Serial('COM3', timeout=1)


##### PROCEDURES PRATIQUES ######

def trouverInstance() -> None:
    '''
    Ajoute tous les processus ouverts dans une liste afin de chercher si code.exe est ouvert ou non.
    On l'ouvre s'il n'est pas déjà ouvert
    '''
    #On crée une instance de WMI()
    f = wmi.WMI()
    #On crée une liste contenant tous les processus lancés
    pr = [process.name for process in f.Win32_Process()]
    #Afin de ne pas lancer Code à chaque fois, on ne l'ouvre que s'il n'est pas déjà ouvert
    if "Code.exe" not in pr:
        os.startfile("C:\\Program Files\\Microsoft VS Code\\Code.exe")


##### PROGRAMME PRINCIPAL ######



if __name__ == "__main__":
    while True:
        #Lecture des données envoyées sur le port série et comparaison avec une chaîne de caractère en binaire
        if ard.readline() == b'D\xc3\xa9tect\xc3\xa9\r\n':
            trouverInstance()
            #Appel de fonctions contenues dans voice_commands.py
            voice_commands.wishMe()       
            voice_commands.voice_cmd()     

# TODO #5 : Commente ton code pour qu'il soit compréhensible
# TODO : Termine les docstrings