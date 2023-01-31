import numpy as np
import pickle
import pandas as pd
import streamlit as st
import joblib
import time
import smtplib as s

    
import smtplib
from email.mime.text import MIMEText

st.sidebar.markdown("Welcome to MLB player salary prediction application! Please login or request a new password via email.")
act = ["Login", "Request password"]
choice = st.sidebar.selectbox("Reset Password", act)

if choice == "Login":
    st.markdown("add code")

elif choice == "Request password":
    st.title("Send password to email")
    sender = "ajflash21@gmail.com"
    password = "Offutlake2017"
    reciever = st.text_input("Enter your email address")
    button = st.button("Send email")
    if button:
        connection =s.SMTP('smtp.gmail.com', 587)
        connection.starttls()
        connection.login(sender,password)
        connection.sendmail(sender, reciever)
        connection.quit()
        



           
    
