import streamlit as st
import pandas as pd

st.title("Videojuegos populares 1980-2023")

data = pd.read_csv('games.csv')
dg = pd.DataFrame(data)
dg
rating = st.selectbox('Valoración',(dg['Rating'].sort_values(ascending=True).unique()))

filtro = (dg['Rating'] == rating)

dg_filtro = dg.loc[filtro]
dg_filtro = dg_filtro.loc[:,['Rating','Title']]

chart_data = pd.DataFrame(
    dg_filtro,
    columns=["Rating",'Title'])

st.bar_chart(chart_data, y='Rating', x='Title')

