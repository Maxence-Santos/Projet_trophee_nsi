import json
from urllib.request import urlopen
from deep_translator import GoogleTranslator
from bs4 import BeautifulSoup as bs
import requests


def weather():
    with open("conf/ville.txt", "r") as f:
        ville = f.read()
    with open("conf/api_key.txt", "r") as f:
        api_key = f.read()
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={ville}&days=2&aqi=no&alerts=no"
    reponse = urlopen(url)
    data = json.loads(reponse.read())["forecast"]["forecastday"]
    today_weather = {"temp_min": int(data[0]["day"]["mintemp_c"]),
                     "temp_max": int(data[0]["day"]["maxtemp_c"]),
                     "vent": int(data[0]["day"]["maxwind_kph"]),
                     "description": GoogleTranslator(source="english",
                                                     target="fr").translate(
                         data[0]["day"]["condition"]["text"]
                     )
                     }
    tomorrow_weather = {"temp_min": int(data[1]["day"]["mintemp_c"]),
                        "temp_max": int(data[1]["day"]["maxtemp_c"]),
                        "vent": int(data[1]["day"]["maxwind_kph"]),
                        "description": GoogleTranslator(source="english",
                                                        target="fr").translate(
                            data[1]["day"]["condition"]["text"]
                        )
                        }
    rapport = f"""
Aujourd'hui, les températures iront de {today_weather['temp_min']} à {today_weather['temp_max']} degrés.
Le vent soufflera jusqu'à {today_weather['vent']} km/h. La tendance de la journée est : {today_weather['description']}.
Demain, les températures iront de {tomorrow_weather['temp_min']} à {tomorrow_weather['temp_max']} degrés.
Le vent soufflera jusqu'à {tomorrow_weather['vent']} km/h. La tendance de la journée sera : {tomorrow_weather['description']}.
"""
    return rapport


def actus():
    with open("conf/topics.json", "r") as f:
        file = json.loads(f.read())
        topics = file["topics"]
        nb_articles = file["nb_articles"]
    url = "https://www.20minutes.fr/"
    articles = []
    for topic in topics:
        topic_url = url + topic
        reponse = requests.get(topic_url)
        data = bs(reponse.content, 'html.parser')
        headlines = data.find_all("div", class_="teaser-headline")
        titres = data.find_all("h2", class_="teaser-title")
        summary = data.find_all("p", class_="teaser-summary")
        article_topic = [article for article in zip(headlines, titres, summary)]
        articles += article_topic[:nb_articles]
    articles = list(set(articles))
    rapport = ""
    for article in articles:
        headline = article[0].get_text()
        titre = article[1].get_text()
        resume = article[2].get_text()
        rapport += f"{headline} : {titre}. {resume}.\n"
    return rapport


if __name__ == "__main__":
    print(actus())
