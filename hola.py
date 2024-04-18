import streamlit as st
import pandas as pd

#Creasmos el titulo de la App
st.title('Titanic App')
st.header('Titanic Graphs - App')
st.write("GRAPHICS OF THE TITANIC DATASET")

titanic_link = 'Titanic.csv'
titanic_data = pd.read_csv(titanic_link)
st.dataframe(titanic_data.sample(10))