import datetime as dt
import re
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
from PIL import Image


# Set page title
st.title('User Engagement analysis')
clusters = pd.read_csv("data/clusters.csv")
st.subheader('Cluster 0 Mean, Max, and Total')
st.dataframe(clusters[:4].drop(["Kth Group"], axis=1))

st.subheader('Cluster 1 Mean, Max, and Total')
st.dataframe(clusters[4:7].drop(["Kth Group"], axis=1))

st.subheader('Cluster 2 Mean, Max, and Total')
st.dataframe(clusters[7:].drop(["Kth Group"], axis=1))

handset_all = Image.open('images/handset_manufacturer.png')
top_three_types = Image.open("images/three_manufacturer_type.png")
top_twenty_handset = Image.open("images/top 20 handsets.png")
top_three_handset_manufactureres = Image.open(
    "images/top_3_handset_manufacturers.png")


st.image(handset_all, caption='All Handsets')
st.image(top_three_types, caption="Top three manufacturers")
st.image(top_twenty_handset, caption="Top 20 Handsets")
st.image(top_three_handset_manufactureres, caption="Top Handset Manufacturers")
