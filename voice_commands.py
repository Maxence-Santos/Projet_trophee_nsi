import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import keyboard
import fnmatch
import pathlib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 18:
        speak('Bonjour')

    else:
        speak('Bonsoir')

    speak('Comment puis-je vous aider')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        speak("Je vous écoute")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        speak("reconnaissance en cours")
        query = r.recognize_google(audio, language='fr-ln')
        print(query)

    except Exception as e:
        speak("pouvez-vous répéter")
        query = takeCommand().lower()
        return query
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.free.fr', 993)
    server.ehlo()
    server.starttls()
    server.login('maxence1405@free.fr', '28091411')
    server.sendmail('maxence1405@free.fr',to,content)
    server.close()
    """server = smtplib.SMTP('localhost')
    server.sendmail("maxence1405@free.fr",to,content)
    server.quit()"""

def mode_normal():
    while True:
        query = takeCommand().lower()
        if 'qui est' in query:
            speak('recherche wikipedia...')
            query = query.replace("wikipedia","")
            wikipedia.set_lang("fr")
            results = wikipedia.summary(query,sentences=2)
            speak("d'après Wikipedia")
            print(results)
            speak(results)

        elif "youtube" in query:
            song = query.replace('youtube','')
            pywhatkit.playonyt(song,True)

        elif "google" in query:
            os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

        elif "météo" in query:
            webbrowser.open_new_tab("https://meteofrance.com")

        elif "pronote" in query:
            webbrowser.open_new_tab("https://0332870r.index-education.net/pronote/eleve.html")
        
        elif "joue" in query:
            music_dir = "D:\\Documents\\Musique"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "heure" in query:
            speak("Il est"+datetime.datetime.now().strftime("%H")+"heures"+datetime.datetime.now().strftime("%M"))
        
        elif "code" in query:
            os.startfile("C:\\Programmes\\Microsoft VS Code\\Code.exe")

        elif "mail" in query:
            try:
                speak("Qu'est-ce que vous voulez dire")
                content = takeCommand()
                to = "richard.jean-francoi@orange.fr"
                sendEmail(to,content)
                speak("L'email a été envoyé")
            except Exception as e:
                print(e)
                speak("Désolé, je n'ai pas pu envoyer le mail")

        elif "recherche" in query:
            recherche = query.replace("recherche","")
            pywhatkit.search(recherche)
        
        elif "bouton" in query:
            speak("mode bouton activé")
            mode_bouton()
            

def mode_bouton():
    t = True
    while t:
        try:
            if keyboard.is_pressed(':'):
                query = takeCommand().lower()
                if 'qui est' in query:
                    speak('recherche wikipedia...')
                    query = query.replace("wikipedia","")
                    wikipedia.set_lang("fr")
                    results = wikipedia.summary(query,sentences=2)
                    speak("d'après Wikipedia")
                    print(results)
                    speak(results)

                elif "youtube" in query:
                    song = query.replace('youtube','')
                    pywhatkit.playonyt(song,True)

                elif "google" in query:
                    os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

                elif "météo" in query:
                    webbrowser.open_new_tab("https://meteofrance.com")

                elif "pronote" in query:
                    webbrowser.open_new_tab("https://0332870r.index-education.net/pronote/eleve.html")
                
                elif "joue" in query:
                    music_dir = "D:\\Documents\\Musique"
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))

                elif "heure" in query:
                    speak("Il est"+datetime.datetime.now().strftime("%H")+"heures"+datetime.datetime.now().strftime("%M"))
                
                elif "code" in query:
                    os.startfile("C:\\Programmes\\Microsoft VS Code\\Code.exe")

                elif "mail" in query:
                    try:
                        speak("Qu'est-ce que vous voulez dire")
                        content = takeCommand()
                        to = "richard.jean-francoi@orange.fr"
                        sendEmail(to,content)
                        speak("L'email a été envoyé")
                    except Exception as e:
                        print(e)
                        speak("Désolé, je n'ai pas pu envoyer le mail")

                elif "recherche" in query:
                    recherche = query.replace("recherche","")
                    pywhatkit.search(recherche)

                elif "normal" in query:
                    speak("mode normal activé")
                    mode_normal()
                    t = False
        except:
            break

if __name__ == '__main__':
    wishMe()
    mode_normal()    