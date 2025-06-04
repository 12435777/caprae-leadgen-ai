import streamlit as st
import sqlite3
import joblib
import pandas as pd

model = joblib.load("ml_model/trained_model.pkl")
conn = sqlite3.connect("lead_demo.db")
df = pd.read_sql("SELECT * FROM leads", conn)

st.title("Caprae Lead Generator AI")
st.write("## 📊 Lead Preview")
st.dataframe(df)

st.write("## 🔎 Predict Lead Interest")
name = st.text_input("Name")
email = st.text_input("Email")

if st.button("Predict"):
    input_df = pd.DataFrame([[len(name), len(email)]], columns=["name_len", "email_len"])
    prediction = model.predict(input_df)
    st.success("Interested" if prediction[0] == 1 else "Not Interested")
