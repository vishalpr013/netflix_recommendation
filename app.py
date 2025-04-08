import streamlit as st
import pandas as pd
import requests
import pickle

# Load movie data and cosine similarity matrix
with open('movie_data.pkl', 'rb') as file:
    movies, cosine_sim = pickle.load(file)

# Recommendation function
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return movies[['title', 'movie_id']].iloc[movie_indices]

st.markdown("<h2 style='color: #0A6BCB; font-weight: semibold;'>🎬 Movie Recommendation System</h1>",unsafe_allow_html=True)
selected_movie = st.selectbox('Select a movie:', movies['title'].values)

if st.button('Recommend'):
    recommendations = get_recommendations(selected_movie)

    for i in range(len(recommendations)):
        movie_title = recommendations.iloc[i]['title']
        st.write(f"#### {movie_title}")
