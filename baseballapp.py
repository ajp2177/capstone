import numpy as np
import pickle
import pandas as pd
import streamlit as st
import joblib
import time
import smtplib as s

import streamlit as st
import smtplib

def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Submit"):
        if username == "admin" and password == "admin":
            st.success("Successful login!")
        else:
            st.error("Incorrect username or password")
    if st.button("Reset password"):
        reset_password()

def reset_password():
    st.write("Enter your email address to reset your password:")
    email = st.text_input("Email")
    if st.button("Submit"):
        # send password reset email to the provided email address
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login("<sender's email>", "<email password>")
            subject = "Password Reset"
            body = "Please follow the link to reset your password: <link to password reset page>"
            msg = f"Subject: {subject}\n\n{body}"
            server.sendmail("<sender's email>", email, msg)
            st.success("Password reset email sent!")
        except:
            st.error("Failed to send email")
        finally:
            server.quit()

st.title("Login")
login()
    
    
    
    
   
        



           
    
