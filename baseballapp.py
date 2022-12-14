import numpy as np
import pickle
import pandas as pd
import streamlit as st
import joblib
import time

st.title("Predicting MLB Contracts and Salaries")

st.sidebar.button("help")


#st.image("https://media.istockphoto.com/photos/rear-view-of-baseball-batter-and-catcher-watching-the-pitch-picture-id1174867119?b=1&k=20&m=1174867119&s=170667a&w=0&h=Lpk2muXoNKWB8dTpak55rqwM1ffEddzgSZsmJeZKEvg=", use_column_width= 'always')

# Title
st.title("Predicting MLB Batter Salaries")

# Subtitle
st.markdown("Enter the following statistics for a batter and \
                    get an estimated salary value.")

# Add sidebar
st.sidebar.markdown("## Predict the Salary of a MLB Hitter!")
#st.sidebar.image("http://cdn.shopify.com/s/files/1/0480/9470/7866/collections/ef26964ae31041325cd9672682c01534.jpg?v=1646869133", width = 200)
st.sidebar.markdown("How does a team determine how much to pay their players?")

# input bar 1
difference = st.number_input("Average Salary Difference (in $)")
st.caption("*Note: Average Salary Difference is the average increase/decrease of a salary across a player's entire career. \
For example, Derek Jeter's Average Salary Difference between 2012 and 2013 would be \\$1M if his salary was \\$14M in 2012 and \\$15M in 2013")

# input bar 2
age = st.slider('Age', 18, 45, 25)

# input bar 3
hits = st.slider('Hits', 0, 250, 100)

# input bar 4
runs= st.slider('Runs', 0, 200, 50)

# input bar 5
rbi = st.slider('RBIs', 0, 200, 75)

# input bar 6
walks = st.slider('Walks', 0, 250, 50)

# input bar 7
so = st.slider('Strikeouts', 0, 250, 50)

# input bar 8
sb = st.slider('Stolen Bases', 0, 100, 10)

# input bar 9
ops = st.number_input("Enter OPS")

# if button is pressed
if st.button("Submit"):

    # unpickle the batting model
    bb_model = joblib.load("batting_basic_model.pkl")

    # store inputs into df

    column_names = ['Salary Difference', 'Age', 'H', 'R', 'RBI', 'BB', 'SO', 'SB', 'OPS']
    df = pd.DataFrame([[difference, age, hits, runs, rbi, walks, so, sb, ops]], 
                     columns = column_names)

    
