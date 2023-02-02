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
#The follow resource was used to help add security to the application   
#Streamlit. (n.d.). *Authentication Without SSO*. Streamlit. https://docs.streamlit.io/knowledge-base/deploy/authentication-without-sso


if check_password():

    st.sidebar.info("Welcome, please use dropdown box to navigate to other pages.")

    pages = ["Home", "Data Exploration", "Predict Player Salary"]
    message = '''Select one of the options in the dropdown list to access specific page'''
    choice = st.sidebar.selectbox("Choose a page: ",pages, help = message)
    listo = ['','Page Description', 'Ways to navigate app', 'About app']

    if choice == "Home":
        st.sidebar.markdown("**Help:** ")
        learn =  st.sidebar.selectbox("What would you like assistance with?", listo)
        if learn == 'Page Description':
            st.sidebar.markdown('This is the home page of the application to access other pages including Data Exploration and Predict Player Salary use the "Choose a page" dropdown list above.') 
        elif learn == 'Ways to navigate app':
            st.sidebar.markdown('1. To navigate to different pages use the "use the "Choose a page" dropdown list above. 2. To navigate between elements on a page, click on the desired tab at the top of the page.')
        elif learn == 'About app':
            st.sidebar.markdown('This app serves to provide insights into MLB player salaries and the value of players through gradient boosting regression.')
                                
                             
        
        
        
        st.markdown("<h1 style='text-align: center; color: green;'>The Value of MLB Players</h1>", unsafe_allow_html=True)

        st.image('http://bronxpinstripes.com/wp-content/uploads/2020/06/MLB-Betting.png')

        st.markdown("This application provides a gradient boosting regression model to predict the salary that should be given to players based on performance metrics.", unsafe_allow_html=True)


    elif choice == "Data Exploration":
        tab1, tab2 = st.tabs(["Exploratory Analysis", "Data Visualizations"])
        learn =  st.sidebar.selectbox("What would you like assistance with?", listo)
        if learn == 'Page Description':
            st.sidebar.markdown('This is the Data Exploration page of the application to view some visualizations regarding the MLB data.')
        elif learn == 'Ways to navigate app':
            st.sidebar.markdown('1. To navigate to different pages use the "use the "Choose a page" dropdown list above. 2. To navigate between elements on a page, click on the desired tab at the top of the page.')
        elif learn == 'About app':
            st.sidebar.markdown('This app serves to provide insights into MLB player salaries and the value of players through gradient boosting regression.')
                                
        with tab1:
                df = pd.read_csv('df')
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
                
                st.markdown('**The average MLB salary is  $5,553,397.74**')
                
                code = '''import statistics
meansal = statistics.mean(df2.salary)
print('The average MLB salary is ', '${:,.2f}'.format(meansal))'''
                st.markdown("**Code:**")
                st.code(code, language='python')
                


                
                
        with tab2:  
            sc = st.selectbox("Select a plot to visualize: ", ('WAR Stat Values',
                                                                         'Most Common MLB Salary Values',
                                                                         "Position Group Totals",
                                                                         ))

            if sc == 'WAR Stat Values':
                 st.image("Screen Shot 2023-02-01 at 3.27.21 PM.png")

            elif sc == 'Most Common MLB Salary Values':
                st.image("Screen Shot 2023-02-01 at 3.30.17 PM.png")

            elif sc == 'Position Group Totals':
                st.image("Screen Shot 2023-02-01 at 3.35.46 PM.png")

    elif choice == "Predict Player Salary":

        st.markdown("<h1 style='text-align: left; color: green;'>Predict MLB Player Salaries</h1>", unsafe_allow_html=True)

        st.image("https://cdn.vox-cdn.com/thumbor/BROKHvXvRY7VPqC2opTqGjKIksI=/1400x1050/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/13688709/TeamsHoardingCash_Getty_Ringer.jpg")
        learn =  st.sidebar.selectbox("What would you like assistance with?", listo)
        if learn == 'Page Description':
            st.sidebar.markdown('This is the Predict Player page to generate player salaries based on the selected input.') 
        elif learn == 'Ways to navigate app':
            st.sidebar.markdown('1. To navigate to different pages use the "use the "Choose a page" dropdown list above. 2. To navigate between elements on a page, click on the desired tab at the top of the page.')
        elif learn == 'About app':
            st.sidebar.markdown('This app serves to provide insights into MLB player salaries and the value of players through gradient boosting regression.')
        #st.markdown('**Select the Hitters or Pitchers tab to predict player salaries**')                       
        #tab3, tab4 = st.tabs(["Hitters", "Pitchers"])

        #with tab3:
        st.markdown("Input or slide the hitting performance values then click Predict Salary")

        age = st.slider('Age', 18, 45, 27)


        bb = st.slider('BB', 0, 140, 70)


        rbis = st.slider('RBIs', 0, 140, 50)


        ibb = st.slider('Intentional Walks', 0, 20, 5)

        hr = st.slider('HR', 0, 65, 10)

        infobp ='''OBP ranges from .200 to 0.550'''

        obp = st.number_input('Enter OBP', min_value=0.200, max_value=0.550, value=0.331, help=infobp)

        infops ='''OBS ranges from .555 to 1.425'''

        ops = st.number_input("OPS", min_value=0.555, max_value=1.425, value=0.800, help=infops)

        sd = st.number_input("Salary Difference")


        # if button is pressed
        if st.button("Predict Salary"):
            gbr = joblib.load("df_model.pkl")

            cn = ['age', 'bb', 'rbis', 'obp', 'ops', 'ibb', 'hr', 'sd']
            df = pd.DataFrame([[age, bb, rbis, obp, ops, ibb, hr, sd]], columns = cn)
            #use gradient boosting regression model to predict salary
            grb_pred = gbr.predict(df)
            #compute the exponential of prediction and take the first element of the resulting array then round to the nearest integer
            pred = round(np.exp(grb_pred)[0],0)

            st.dataframe(df)
            #display the predicted salary 
            st.header("Player Salary Prediction $" + format(pred, ","))

            st.markdown("### Predictions compared to 2022 data")
            #utilize 2022 data from baseball-reference
            last_season = pd.read_csv('2022_data', index_col = 0)
            # reformat 2022 batter df for model prediction
            df_to_predict = last_season.drop(columns = ['Name', '2022 Salary'])

            # load in model
            gbr_m = joblib.load("df_model.pkl")

            new_pred = gbr_m.predict(df_to_predict)

            last_season["Predicted Salary"] = np.around(np.exp(new_pred),0)

            #display comparisions
            st.dataframe(last_season)

        

    
