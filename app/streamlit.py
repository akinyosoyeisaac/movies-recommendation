import pandas as pd
import numpy as np
import streamlit as st
from src.models.predict_model import recommender
import requests

def poster(movie_id):
    response = requests.get()

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
    
    
    # recommender(title)

    
if __name__ == "__main__":
    main()