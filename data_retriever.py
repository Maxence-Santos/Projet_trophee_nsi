##### IMPORT DES LIBRAIRIES #####
import json
from urllib.request import urlopen
from deep_translator import GoogleTranslator
from bs4 import BeautifulSoup as bs
import requests


def weather() -> str:
    '''
    Fait un rapport météo succinct de la journée et du lendemain
    Paramètres:
        - None
    Retour :
        - str : Le rapport météo
    '''
    # Note la ville où le rapport météo devra être fait ainsi que la clé API
    with open("config.json", "r") as f:
        file = json.loads(f.read())
        ville = file["ville"]
        api_key = file["api_key"]
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={ville}&days=2&aqi=no&alerts=no"
    reponse = urlopen(url)  # Ouvre la page du rapport météo
    data = json.loads(reponse.read())["forecast"]["forecastday"]
    # Crée un dictionnaire des informations qui seront utiles au rapport ( températures, vent, description )
    today_weather = {"temp_min": int(data[0]["day"]["mintemp_c"]),
                     "temp_max": int(data[0]["day"]["maxtemp_c"]),
                     "vent": int(data[0]["day"]["maxwind_kph"]),
                     "description": GoogleTranslator(source="english",
                                                     target="fr").translate(
                         data[0]["day"]["condition"]["text"]
                     )
                     }
    # Fait de même avec les conditions du lendemain
    tomorrow_weather = {"temp_min": int(data[1]["day"]["mintemp_c"]),
                        "temp_max": int(data[1]["day"]["maxtemp_c"]),
                        "vent": int(data[1]["day"]["maxwind_kph"]),
                        "description": GoogleTranslator(source="english",
                                                        target="fr").translate(
                            data[1]["day"]["condition"]["text"]
                        )
                        }
    # Reformate les données pour en fait un rapport
    rapport = f"""
Aujourd'hui, les températures iront de {today_weather['temp_min']} à {today_weather['temp_max']} degrés.
Le vent soufflera jusqu'à {today_weather['vent']} km/h. La tendance de la journée est : {today_weather['description']}.
Demain, les températures iront de {tomorrow_weather['temp_min']} à {tomorrow_weather['temp_max']} degrés.
Le vent soufflera jusqu'à {tomorrow_weather['vent']} km/h. La tendance de la journée sera : {tomorrow_weather['description']}.
"""
    return rapport


def actus() -> str:
    '''
        Fait un rapport des actualités succinct
        Paramètres:
            - None
        Retour :
            - str : Le rapport des actualités
        '''
    # Ouvre le fichier de configuration pour noter les sujets d'intérêts de l'utilisateur et la qté d'aticles à donner
    with open("config.json", "r") as f:
        file = json.loads(f.read())
        topics = file["topics"]
        nb_articles = file["nb_articles"]
    url = "https://www.20minutes.fr/"
    articles = []
    for topic in topics:
        topic_url = url + topic
        reponse = requests.get(topic_url)
        # Passe le résultats de la requête dans BS pour pouvoir manipuler les éléments html
        data = bs(reponse.content, 'html.parser')
        # Récupère les titres et résumé en fonction des classes trouvées en inspectant le code source du site
        headlines = data.find_all("div", class_="teaser-headline")
        titres = data.find_all("h2", class_="teaser-title")
        summary = data.find_all("p", class_="teaser-summary")
        # Crée une liste de tuples mettant ensemble les titres et résumés
        article_topic = [article for article in zip(headlines, titres, summary)]
        # Enlève les articles en trop en fonction du choix de l'utilisateur
        articles += article_topic[:nb_articles]
    # Enlève les doublons
    articles = list(set(articles))
    rapport = ""
    # Récupère le texte de chaque élément html et les formatte pour créer un rapport
    for article in articles:
        headline = article[0].get_text()
        titre = article[1].get_text()
        resume = article[2].get_text()
        rapport += f"{headline} : {titre}. {resume}.\n"
    return rapport


if __name__ == "__main__":  # Sert seulement pour tester les fonctions
    print(weather())
    print(actus())

# TODO : Gérer les erreurs
