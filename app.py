import streamlit as st
import pickle
import pandas as pd
import requests 

similarity = pickle.load(open('similarity.pkl','rb'))
movies_list_data = pickle.load(open('movie.pkl','rb'))
movies_list = movies_list_data['title'].values
st.title('Movie Recommender System')

def fetch_poster(movie_id):




def recommend(movie,movies_list):
    movie_index = movies_list_data[movies_list_data['title'] == movie].index[0]
    distaces = similarity[movie_index]
    movies_with_distances = sorted(list(enumerate(distaces)),reverse=True,key = lambda x:x[1])[1:6]
    recommended_movie = []
    recommended_posters = []
    for i in movies_with_distances:
        recommended_movie.append(movies_list[i[0]])
        recommended_posters.append(fetch_poster(i[0]))
    return recommended_movie


selection_movie_name = st.selectbox(
'Recommed movies',movies_list
)
if st.button('Recommend'):
    recommendations = recommend(selection_movie_name,movies_list)
    for i in recommendations:
        st.write(i)