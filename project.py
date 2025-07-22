import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_excel("training_data_100.xlsx")

to_URL = {
    'English Hub':'https://discord.gg/enghub',
    'English': 'https://discord.gg/english',
    'The Entrepreneur Network':'https://discord.gg/the-entrepreneur-network-beta-1164702592241238178',
    'Travel Hub':''
}

# Encode text data
le_goal = LabelEncoder()
le_cert = LabelEncoder()
le_mode = LabelEncoder()
le_focus = LabelEncoder()
le_server = LabelEncoder()

df['Goal'] = le_goal.fit_transform(df['Goal'])
df['CertSupport'] = le_cert.fit_transform(df['CertSupport'])
df['Mode'] = le_mode.fit_transform(df['Mode'])
df['Focus'] = le_focus.fit_transform(df['Focus'])
df['RecommendedServer'] = le_server.fit_transform(df['RecommendedServer'])

# Load the trained model
model = joblib.load('decision_tree_model.pkl')

# Streamlit UI
st.markdown("""
Answer a few questions and get a personalized recommendation for a language learning Discord server or course.
""")

# User inputs
age = st.number_input(" Your age:", min_value=10, max_value=100, step=1)

goal = st.selectbox(" Your learning goal:", le_goal.classes_)

cert = st.radio("Do you need support for language certificates (like IELTS/TOEFL)?", le_cert.classes_)

mode = st.selectbox("Your preferred learning mode:", le_mode.classes_)

focus = st.selectbox("What would you like to focus on?", le_focus.classes_)

# Prediction button
if st.button("Recommend me a server"):
    input_data = pd.DataFrame([{
        'Age': age,
        'Goal': int(le_goal.transform([goal])[0]),
        'CertSupport': int(le_cert.transform([cert])[0]),
        'Mode': int(le_mode.transform([mode])[0]),
        'Focus': int(le_focus.transform([focus])[0])
    }])
    
    prediction = model.predict(input_data)[0]
    server_name = le_server.inverse_transform([prediction])[0]

    st.success(f"Recommended server for you: **{server_name}**: {to_URL[server_name]}")
