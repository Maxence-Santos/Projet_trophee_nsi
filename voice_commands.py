##### IMPORT DES LIBRAIRIES #####
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
    '''
    Dit "Bonjour" ou "Bonsoir" en fonction de l'heure qu'il est et
    demande à l'utilisateur en quoi il peut l'aider.
    Retour :
        -None
    '''
    #On récupère l'heure actuelle
    hour = int(datetime.datetime.now().hour)
    #S'il est entre minuit et 18 heures le programme dit "Bonjour"
    if hour >= 0 and hour < 18:
        speak('Bonjour')

    else:
        speak('Bonsoir')

    speak('Comment puis-je vous aider')

def takeCommand():
    '''
    Permet au programme de prendre une entrée audio et de reconnaître ce qui a été dit.
    Retour :
        - Chaîne de caractères
    '''
    #Création d'une instance de Recongizer()
    r = sr.Recognizer()
    #On initialise le microphone de l'ordinateur comme entrée audio
    with sr.Microphone() as source:
        print("Écoute en cours... ")
        speak("Je vous écoute")
        r.pause_threshold = 1
        audio = r.listen(source)
    try: 
        print("Reconnaissance...")
        speak("reconnaissance en cours")
        #On récupère l'instruction de l'utilisateur
        query = r.recognize_google(audio, language='fr-ln')
        print(query)

    except Exception as e:
        speak("pouvez-vous répéter")
        query = takeCommand().lower()
        return query
    return query        
            

def voice_cmd():
    '''
    Fonction permettant de répondre aux instructions de l'utilisateur.
    Retour :
        - None
    '''
    running = True 
    mode_bouton = False
    while running:
            #On vérifie si on est en mode bouton ou non avant de triter l'instruction
            if (mode_bouton and keyboard.is_pressed(':')) or not mode_bouton:
                query = takeCommand().lower()
                #Définition de l'expression permettant de lancer une recherche wikipédia
                if 'qui est' in query:
                    speak('recherche wikipedia...')
                    #On enlève le mot "wikipédia" de l'instruction 
                    query = query.replace("wikipedia","")
                    wikipedia.set_lang("fr")
                    #On récupère un résumé de la page wikipédia
                    results = wikipedia.summary(query,sentences=2)
                    speak("d'après Wikipedia")
                    print(results)
                    speak(results)

                #Définition de l'expression permettant de lancer une vidéo sur youtube
                elif "youtube" in query:
                    song = query.replace('youtube','')
                    #Appel à la fonction de la librairie permettant de lancer la cidéo demandée sur youtube
                    pywhatkit.playonyt(song)

                #Définition des expressions permettant d'appeler la fonction de data_retreiver.py permettant de donner la météo'
                elif any(word in query for word in ["météo","temps"]):
                    speak(data_retriever.weather())

                #Définition des expressions permettant d'appeler la fonction de data_retreiver.py permettant de donner les actualités
                elif any(word in query for word in ["actu","actus","news","actualités","informations"]):
                    speak(data_retriever.actus())

                #Définition de l'expression permettant de lancer pronote
                elif "pronote" in query:
                    webbrowser.open_new_tab("https://0332870r.index-education.net/pronote/eleve.html")
                
                #Définition de l'expression permettant de lancer les chansons du dossier "Musique"
                elif "joue" in query:
                    music_dir = "D:\\Documents\\Musique"
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))

                #Définition de l'expression permettant de donner l'heure
                elif "heure" in query:
                    speak("Il est"+datetime.datetime.now().strftime("%H")+"heures"+datetime.datetime.now().strftime("%M"))
                
                #Définition de l'expression permettant de lancer Code.exe
                elif "code" in query:
                    os.startfile("C:\\Programmes\\Microsoft VS Code\\Code.exe")

                #Définition de l'expression permettant de lancer une recherche sur internet
                elif "recherche" in query:
                    recherche = query.replace("recherche","")
                    pywhatkit.search(recherche)
                
                #Définition de l'expression permettant de lancer le "mode bouton"
                elif "bouton" in query:
                    speak("mode bouton activé")
                    #On active le mode bouton
                    mode_bouton = True

                #Définition de l'expression permettant de relancer le "mode normal"
                elif "normal" in query:
                    speak("mode bouton activé")
                    #On désactive le "mode bouton"
                    mode_bouton = False

                #Définition des expressions permettant d'arrêter l'assistant vocal
                elif any(word in query for word in ["éteins","éteint","éteindre"]):
                    running = False
                    speak("Au revoir")
                    
                
##### PROGRAMME PRINCIPAL ######
if __name__ == '__main__':
    wishMe()
    voice_cmd()    