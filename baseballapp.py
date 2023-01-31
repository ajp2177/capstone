import numpy as np
import pickle
import pandas as pd
import streamlit as st
import joblib
import time
import smtplib as s

    
import smtplib
from email.mime.text import MIMEText

def send_email(email, username, password_reset_link):
    # Build the email message
    msg = MIMEMultipart()
    msg['From'] = "your_email_address"
    msg['To'] = email
    msg['Subject'] = "Password Reset"
    body = f"Dear {username},\n\nYou recently requested a password reset for your account. Please use the following link to reset your password:\n\n{password_reset_link}\n\nIf you did not request a password reset, please ignore this email.\n\nBest regards,\nYour team"
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg['From'], "your_email_password")
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    
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

elif choice == "Predict Player Salary":

st.markdown("<h1 style='text-align: left; color: green;'>Predict MLB Player Salaries</h1>", unsafe_allow_html=True)

st.image("https://cdn.vox-cdn.com/thumbor/BROKHvXvRY7VPqC2opTqGjKIksI=/1400x1050/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/13688709/TeamsHoardingCash_Getty_Ringer.jpg")


tab3, tab4 = st.tabs(["Hitters", "Pitchers"])

with tab3:
    st.markdown("Input or slide the hitting performance values then click Predict Salary")
    difference = st.number_input("Salary Difference")


    age = st.slider('Age', 18, 45, 27)


    hits = st.slider('Hits', 0, 250, 100)


    runs= st.slider('Runs', 0, 200, 50)


    rbi = st.slider('RBIs', 0, 200, 75)


    walks = st.slider('Walks', 0, 250, 50)


    so = st.slider('Strikeouts', 0, 250, 50)

    sb = st.slider('Stolen Bases', 0, 100, 10)


    ops = st.number_input("Enter OPS")

    # if button is pressed
    if st.button("Predict Salary"):

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

        st.markdown("### Predictions compared to 2022 data")


        # 2022 batter dataframe
        data_2022 = pd.read_csv('batting_merged_2022', index_col = 0)
        # reformat 2022 batter df for model prediction
        df_to_predict = data_2022.drop(columns = ['Name', '2022 Salary'])

        # load in model
        model = joblib.load("batting_basic_model.pkl")

        # make prediction
        predictions_2022 = model.predict(df_to_predict)

        # Add prediction column
        data_2022["Predicted Salary"] = np.around(np.exp(predictions_2022),0)

        # Add value column
        data_2022.loc[data_2022['Predicted Salary'] > data_2022['2022 Salary'], 'Value?'] = 'Under-valued'
        data_2022.loc[data_2022['Predicted Salary'] < data_2022['2022 Salary'], 'Value?'] = 'Over-valued'

        # reorder columns
        data_2022 = data_2022[['Name', '2022 Salary', 'Predicted Salary', 'Value?', 'Avg Career Salary Difference', 'Age', \
                                        'H', 'R', 'RBI', 'BB', 'SO', 'SB', 'OPS']]

        # formatting as Millions
        data_2022['2022 Salary'] = data_2022['2022 Salary']
        data_2022['Predicted Salary'] = data_2022['Predicted Salary']
        data_2022['Avg Career Salary Difference'] = data_2022['Avg Career Salary Difference']

        data_2022 = data_2022.rename(columns = {'2022 Salary':'2022 Salary ($ Millions)',
                                                          'Predicted Salary':'Predicted Salary ($ Millions)',
                                                          'Salary Difference':'Avg Career Salary Difference ($ Millions)'})

        st.dataframe(data_2022)


           
    
