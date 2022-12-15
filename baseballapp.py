import numpy as np
import pickle
import pandas as pd
import streamlit as st
import joblib
import time


def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.subheader("**Enter password to access application**")
        st.text_input(
            "Password:", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("Incorrect password, please try again.")
        return False
    else:
        # Password correct.
        return True


if check_password():
    
  st.sidebar.info("Welcome, please use dropdown box to navigate to other pages.")

  pages = ["Home", "Data Exploration", "Predict Player Salary"]
  message = '''Select one of the options in the dropdown list to access specific page'''
  choice = st.sidebar.selectbox("Choose a page: ",pages, help = message)
  listo = ['','Page Description', 'How to access different pages', 'About app']

  if choice == "Home":
    st.sidebar.markdown("**Help:** ")
    learn =  st.sidebar.selectbox("What would you like assistance with?", listo)
    st.markdown("<h1 style='text-align: center; color: green;'>The Value of MLB Players</h1>", unsafe_allow_html=True)

    st.image('https://www.sportico.com/wp-content/uploads/2022/04/Valuation_List_1280x720-1.png?w=1280&h=720&crop=1')

    st.markdown("This application provides a model to predict the salary that should be given to players based on performance metrics.", unsafe_allow_html=True)

    
  elif choice == "Data Exploration":
    tab1, tab2 = st.tabs(["Exploratory Analysis", "Data Visualizations"])
    
    with tab1:
            df = pd.read_csv('batting_basic')
            dataframe = st.dataframe(df)

            @st.experimental_memo
            def convert_df(df):
                return df.to_csv(index=False).encode('utf-8')


            csv = convert_df(df)

            st.download_button(
                "Download dataset",
                csv,
                "file.csv",
                "text/csv",
                key='download-csv'
            )
        #elif option == "
    with tab2:  
        sc = st.selectbox("Select a plot to visualize: ", ('Histogram',
                                                                     'Boxplots',
                                                                     "Position Group Totals",
                                                                     ))
        if sc == 'Histogram':
            st.image("Screen Shot 2022-12-14 at 11.01.57 PM.png")
            
        elif sc == 'Boxplots':
            st.image("Screen Shot 2022-12-14 at 11.16.28 PM.png")
        
        elif sc == 'Position Group Totals':
            st.image("Screen Shot 2022-12-14 at 11.10.29 PM.png")
            
            
st.markdown("### Predictions compared to 2022 data")


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
batter_2022_df['2022 Salary'] = batter_2022_df['2022 Salary'].div(1000000).round(2)
batter_2022_df['Predicted Salary'] = batter_2022_df['Predicted Salary'].div(1000000).round(2)
batter_2022_df['Avg Career Salary Difference'] = batter_2022_df['Avg Career Salary Difference'].div(1000000).round(2)

batter_2022_df = batter_2022_df.rename(columns = {'2022 Salary':'2022 Salary ($ Millions)',
                                                  'Predicted Salary':'Predicted Salary ($ Millions)',
                                                  'Avg Career Salary Difference':'Avg Career Salary Difference ($ Millions)'})

st.dataframe(batter_2022_df)


           
    
