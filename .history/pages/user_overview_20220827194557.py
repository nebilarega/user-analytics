import datetime as dt
import re
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
from PIL import Image


# Set page title
st.title('User Overview Analysis')
st.subheader('Manufacturers and Handsets')
handset_all = Image.open('images/handset_manufacturer.png')
top_three_types = Image.open("images/three_manufacturer_type.png")
top_twenty_handset = Image.open("images/top 20 handsets.png")
top_three_handset_manufactureres = Image.open(
    "images/top_3_handset_manufacturers.png")


st.image(handset_all, caption='All Handsets')
st.image(top_three_types, caption="Top three manufacturers")
st.image(top_twenty_handset, caption="Top 20 Handsets")
st.image(top_three_handset_manufactureres, caption="Top Handset Manufacturers")
