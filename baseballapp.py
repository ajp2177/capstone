import numpy as np
import pickle
import pandas as pd
import streamlit as st
import joblib
import time
import smtplib as s

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
        st.success("Password reset email sent!")

st.title("Login")
login()
    
    
    
    
   
        



           
    
