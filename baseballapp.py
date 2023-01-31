import numpy as np
import pickle
import pandas as pd
import streamlit as st
import joblib
import time
import smtplib as s

    
import smtplib
from email.mime.text import MIMEText

ebutton = st.button("Send email")

def send_email():
    st.title("Send password to email")
    activities =["Send Email"]
    choice = st.sidebar.selectbox("Reset Password", activites)
    if choice == "Send Email":
        sender = "ajflash21@gmail.com"
        password = "Offutlake2017"
        reciever = st.text_input("Enter your email address")
        if st.buttion("Send Email"):
            try:
                connection =s.SMTP('smtp.gmail.com', 587)
                connection.starttls()
                connection.login(sender,password)
                connection.sendmail(sender, reciever)
                connection.quit()
        



           
    
