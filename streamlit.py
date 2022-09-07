import pandas as pd
import numpy as np
import streamlit as st
from src.models.predict_model import recommender
import requests
import yaml

# loading the configuration parameters
with open("params.yaml") as f:
    config = yaml.safe_load(f)


tmbd_movies = pd.read_csv(config["paths"]["tmdb_movies"])

def movie_id_extract(title: str):
    state = tmbd_movies.title.str.lower().isin([title.lower()]).sum()
    if state == 1:
        movie_id = tmbd_movies.movie_id[tmbd_movies.title.str.lower().isin([title.lower()])].values[0]
    else:
        movie_id = "Movie_title doest not exist in the database at the moment"
    return movie_id
        
def poster(title):
    movie_id = movie_id_extract(title)
    if movie_id != "Movie_title doest not exist in the database at the moment":
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=aa13deff4685a67587afd61223f4714e"
        response = requests.get(url)
        data = response.json()
        return st.image('https://image.tmdb.org/t/p/w500' + data['poster_path'])
    else: 
        return st.write("We can not generate the image at the moment please check back later")

def main():
    st.markdown(
        """
        <style>
        .stApp {background-color: #242582}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("Moive Recommendation System")
    title: str = st.text_input(label="Enter the name of the movie you wish to get recommendation for!", value="The Avengers")
    recommend = st.button(label="Recommend")
    
    if recommend:
        recommendation = recommender(title)
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.write(recommendation[0])
            poster(recommendation[0])
            
        with col2:
            st.write(recommendation[1])
            poster(recommendation[1])
            
        with col3:
            st.write(recommendation[2])
            poster(recommendation[2])
        
        with col4:
            st.write(recommendation[3])
            poster(recommendation[3])
        
        with col5:
            st.write(recommendation[4])
            poster(recommendation[4])
        

    
if __name__ == "__main__":
    main()