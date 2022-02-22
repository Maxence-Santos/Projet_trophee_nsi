import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import keyboard
import data_retriever

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio: str) -> None:
    '''
    Prend une chaîne de caractères en paramètre et la dit à haute voix
    Paramètres:
        - audio : Le chaîne à dire
    Retour :
        None
    '''
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
        print("Écoute en cours... ")
        speak("Je vous écoute")
        r.pause_threshold = 1
        audio = r.listen(source)
    try: 
        print("Reconnaissance...")
        speak("reconnaissance en cours")
        query = r.recognize_google(audio, language='fr-ln')
        print(query)

    except Exception as e:
        speak("pouvez-vous répéter")
        query = takeCommand().lower()
        return query
    return query        
            

def voice_cmd():
    running = True 
    mode_bouton = False
    while running:
            if (mode_bouton and keyboard.is_pressed(':')) or not mode_bouton:
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
                    pywhatkit.playonyt(song)

                elif any(word in query for word in ["météo","temps"]):
                    speak(data_retriever.weather())

                elif any(word in query for word in ["actu","actus","news","actualités","informations"]):
                    speak(data_retriever.actus())

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

                elif "recherche" in query:
                    recherche = query.replace("recherche","")
                    pywhatkit.search(recherche)
                
                elif "bouton" in query:
                    speak("mode bouton activé")
                    mode_bouton = True

                elif "normal" in query:
                    speak("mode bouton activé")
                    mode_bouton = False

                elif any(word in query for word in ["éteins","éteint","éteindre"]):
                    running = False
                    speak("Au revoir")
                    
                

if __name__ == '__main__':
    wishMe()
    voice_cmd()    