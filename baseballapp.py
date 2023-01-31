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
    
    
    
    
   
        



           
    
