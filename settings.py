import streamlit as st
import os
import sys
import json


def save(topics, api_key, ville):
    global status
    if topics != []:
        topics_to_save= {"topics":[]}
        topics_name = ["Actualités générales","Informations nationales", "Sport",
                    "Divertissement", "Économie", "Planète", "Faits insolites",
                    "Desintox", "Tech"]
        correspondances = ["actu-generale","locales","sport","art-stars","economie","planete"
            ,"insolite","desintox","high-tech"]
        for i, topic in enumerate(topics_name):
            if topic in topics:
                topics_to_save["topics"].append(correspondances[i])

        with open("conf/topics.json","w") as f:
            json.dump(topics_to_save, f)
    else:
        status = -1
        return
    with open("conf/ville.txt","w") as f:
        f.write(ville)
    with open("conf/api_key.txt","w") as f:
        f.write(api_key)
    status = 0

st.title("Bienvenue sur la page de configuration")
st.markdown("Pour être sûr que le programme fonctionne, vous devrez configurer quelques paramètres. \
            Vous pouvez toujours accéder à cette page pour changer des paramètres en exécutant **settings.py** .")

st.header("News")
st.markdown("#### Sujets")
topics = st.multiselect("Qu'est-ce qui vous intéresse ? ( vous pouvez choisir autant d'options que vous souhaitez )",
               ["Actualités générales","Informations nationales", "Sport",
                "Divertissement", "Économie", "Planète", "Faits insolites",
                "Desintox", "Tech"],
                        default="Actualités générales")

st.markdown("#### Quantité")
nb_articles = st.slider(f"Nombre d'articles par sujet", 1, 10, 1, 1)
st.caption(f"Avec cette selection, vous aurez {nb_articles*len(topics)} articles en tout à chaque fois")

st.header("Météo")
st.markdown("#### Clé API WeatherAPI")
api_key = st.text_input("Cela nous permettra de récupérer les données météo. Un guide est disponible ci-dessous")
with st.expander("Regardez comment récupérer votre clé API"):
    st.markdown("1. Créer un compte sur [WeatherAPI](https://www.weatherapi.com/signup.aspx) (c'est gratuit!)")
    st.image("img/login.png")
    st.markdown("2. Vérifier votre compte (vous devrez cliquer sur le lien de vérification dans le mail envoyé par WeatherAPI)")
    st.image("img/validate.png")
    st.markdown("3. Allez sur la [page de votre compte](https://www.weatherapi.com/my/) sur laquelle vous trouverez votre clé API (ne la partagez pas !)")
    st.image("img/api.png")
st.markdown("#### Votre ville")
ville = st.text_input("Cela nous permettra de communiquer les données au plus proche de chez vous")

success = st.button("Valider mes choix", on_click=save, args = (topics, api_key, ville))


if success :
    if status==0:
        st.success("Paramètres enregistrés !")
    elif status == -1:
        st.error("Renseignez au moins un sujet qui vous intéresse")
    st.write(status)

if __name__ == "__main__":
    if not st._is_running_with_streamlit:
        os.system(f"streamlit run {sys.argv[0]}")