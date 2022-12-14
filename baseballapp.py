import numpy as np
import pickle
import pandas as pd
import streamlit as st
import joblib
import time

st.title("Predicting MLB Player Salaries")

#st.sidebar.button("help")


st.image("capstonehome.jpeg", use_column_width= 'always')

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
    
      # get prediction
    prediction = bb_model.predict(df)

    # convert prediction
    converted = round(np.exp(prediction)[0],0)

    with st.spinner('Calculating...'):
        time.sleep(1)
    st.success('Done!')

    st.dataframe(df)

    # output prediction
    st.header(f"Predicted Player Salary: ${converted:,}")
    
    
    # header
st.markdown("### How do the predictions compare to 2022 stats thus far?")
st.markdown("###### Updated: Aug 24, 2022")

# 2022 batter dataframe
batter_2022_df = pd.read_csv('batting_merged_2022', index_col = 0)
# reformat 2022 batter df for model prediction
df_to_predict = batter_2022_df.drop(columns = ['Name', '2022 Salary'])

# load in model
bb_model = joblib.load("batting_basic_model.pkl")

# make prediction
predictions_2022 = bb_model.predict(df_to_predict)

# Add prediction column
batter_2022_df["Predicted Salary"] = np.around(np.exp(predictions_2022),0)

# Add value column
batter_2022_df.loc[batter_2022_df['Predicted Salary'] > batter_2022_df['2022 Salary'], 'Value?'] = 'Under-valued'
batter_2022_df.loc[batter_2022_df['Predicted Salary'] < batter_2022_df['2022 Salary'], 'Value?'] = 'Over-valued'

# reorder columns
batter_2022_df = batter_2022_df[['Name', '2022 Salary', 'Predicted Salary', 'Value?', 'Avg Career Salary Difference', 'Age', \
                               'H', 'R', 'RBI', 'BB', 'SO', 'SB', 'OPS']]

# formatting as Millions
batter_2022_df['2022 Salary'] = batter_2022_df['2022 Salary']
batter_2022_df['Predicted Salary'] = batter_2022_df['Predicted Salary'].div(1000000).round(2)
batter_2022_df['Avg Career Salary Difference'] = batter_2022_df['Avg Career Salary Difference'].div(1000000).round(2)

batter_2022_df = batter_2022_df.rename(columns = {'2022 Salary':'2022 Salary ($ Millions)',
                                                 'Predicted Salary':'Predicted Salary ($ Millions)',
                                                 'Avg Career Salary Difference':'Avg Career Salary Difference ($ Millions)'})
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

icon("search")
selected = st.text_input("", "Search...")
button_clicked = st.button("OK")


 
st.dataframe(batter_2022_df)

choice = st.text_input("Search:", key="choice")

if choice == "":
#if nothing is inputed display pandas df as is
    st.dataframe(data=batter_2022_df.head(50), height=600)
else:
    batter_2022_df[batter_2022_df.apply(lambda r: any([kw in r[0] for kw in choice]), axis=1)]







    
