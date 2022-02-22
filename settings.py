##### IMPORT DES LIBRAIRIES #####
import streamlit as st
import os
import sys
import json


def save(topics: list, api_key: str, ville: str, nb_articles: int) -> None:
    '''
    Enregistre dans un fichier les paramètres choisis par l'utilisateur
    :param topics:list - Liste des sujets
    :param api_key:str - Clé API de WeatherAPI
    :param ville:str - Ville où le rapport météo doit être fait
    :param nb_articles:int - Nombre d'articles par sujet
    :return:
    '''
    # S'assure que les paramètres sont corrects
    if api_key != "" and topics != [] and ville != "":
        topics_to_save = {"topics": [], "nb_articles": nb_articles, "api_key": api_key, "ville": ville}
        topics_name = ["Actualités générales", "Informations nationales", "Sport",
                       "Divertissement", "Économie", "Planète", "Faits insolites",
                       "Desintox", "Tech"]
        correspondances = ["actu-generale", "locales", "sport", "art-stars", "economie", "planete"
            , "insolite", "desintox", "high-tech"]
        # Fait l'équivalence entre les noms simplifiés et les noms exacts des sujets
        for i, topic in enumerate(topics_name):
            if topic in topics:
                topics_to_save["topics"].append(correspondances[i])
        # Sauvegarde les paramètre
        with open("config.json", "w") as f:
            json.dump(topics_to_save, f)


##### HEADER #####
st.title("Bienvenue sur la page de configuration")
st.markdown("Pour être sûr que le programme fonctionne, vous devrez configurer quelques paramètres. \
            Vous pouvez toujours accéder à cette page pour changer des paramètres en exécutant **settings.py** .")

##### NEWS #####
st.header("News")
##### Multi-select pour choisir un ensemble de sujets #####
st.markdown("#### Sujets")
topics = st.multiselect("Qu'est-ce qui vous intéresse ? ( choisissez au moins une option )",
                        ["Actualités générales", "Informations nationales", "Sport",
                         "Divertissement", "Économie", "Planète", "Faits insolites",
                         "Desintox", "Tech"],
                        default="Actualités générales")

##### Slider pour indiquer combien d'articles par sujet il faudra énoncer #####
st.markdown("#### Quantité")
nb_articles = st.slider(f"Nombre d'articles par sujet", 1, 10, 1, 1)
st.caption(f"Avec cette selection, vous aurez {nb_articles * len(topics)} articles en tout à chaque fois")

##### MÉTÉO #####
st.header("Météo")
##### Input pour avoir la clé API de l'utilisateur
st.markdown("#### Clé API WeatherAPI")
api_key = st.text_input("Cela nous permettra de récupérer les données météo. Un guide est disponible ci-dessous")
##### Tutoriel déroulable #####
with st.expander("Regardez comment récupérer votre clé API"):
    st.markdown("1. Créer un compte sur [WeatherAPI](https://www.weatherapi.com/signup.aspx) (c'est gratuit!)")
    st.image("img/login.png")
    st.markdown(
        "2. Vérifier votre compte (vous devrez cliquer sur le lien de vérification dans le mail envoyé par WeatherAPI)")
    st.image("img/validate.png")
    st.markdown(
        "3. Allez sur la [page de votre compte](https://www.weatherapi.com/my/) sur laquelle vous trouverez votre clé API (ne la partagez pas !)")
    st.image("img/api.png")
##### Input pour choisir la ville #####
st.markdown("#### Votre ville")
ville = st.text_input("Cela nous permettra de communiquer les données au plus proche de chez vous")

# Bouton pour sauvegarder les paramètres
success = st.button("Valider mes choix", on_click=save, args=(topics, api_key, ville, nb_articles))

# Indiquer le succès de l'opération si les paramètres était valides
if success and api_key != "" and topics != [] and ville != "":
    st.success("Paramètres enregistrés !")
# Afficher une erreur sinon
elif success:
    st.error("Tous les champs doivent être remplis")

# Permet de lancer l'interface utilisateur dans un navigateur si celle-ci n'existe pas déjà
if __name__ == "__main__":
    if not st._is_running_with_streamlit:
        os.system(f"streamlit run {sys.argv[0]}")
