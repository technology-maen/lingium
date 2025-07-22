import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
df = pd.read_excel("training_data_100.xlsx")

# Mapping server names to URLs
to_URL = {
    'English Hub': 'https://discord.gg/enghub',
    'English': 'https://discord.gg/english',
    'The Entrepreneur Network': 'https://discord.gg/the-entrepreneur-network-beta-1164702592241238178',
    'Travel Hub': ''
}

# Initialize label encoders for categorical data
le_goal = LabelEncoder()
le_cert = LabelEncoder()
le_mode = LabelEncoder()
le_focus = LabelEncoder()
le_server = LabelEncoder()

# Encode categorical columns
df['Goal'] = le_goal.fit_transform(df['Goal'])
df['CertSupport'] = le_cert.fit_transform(df['CertSupport'])
df['Mode'] = le_mode.fit_transform(df['Mode'])
df['Focus'] = le_focus.fit_transform(df['Focus'])
df['RecommendedServer'] = le_server.fit_transform(df['RecommendedServer'])

# Load the trained model
model = joblib.load('decision_tree_model.pkl')

# Streamlit UI for user interaction
st.markdown(
    """
    Answer a few questions and get a personalized recommendation for a language learning Discord server or course.
    """
)

# Collect user inputs
age = st.number_input("Your age:", min_value=10, max_value=100, step=1)

goal = st.selectbox("Your learning goal:", list(le_goal.classes_))

cert = st.radio("Do you need support for language certificates (like IELTS/TOEFL)?", list(le_cert.classes_))

mode = st.selectbox("Your preferred learning mode:", list(le_mode.classes_))

focus = st.selectbox("What would you like to focus on?", list(le_focus.classes_))

# Predict and recommend a server based on user inputs
if st.button("Recommend me a server"):
    input_data = pd.DataFrame([
        {
            'Age': age,
            'Goal': le_goal.transform([goal])[0] if goal in le_goal.classes_ else 0,
            'CertSupport': le_cert.transform([cert])[0] if cert in le_cert.classes_ else 0,
            'Mode': le_mode.transform([mode])[0] if mode in le_mode.classes_ else 0,
            'Focus': le_focus.transform([focus])[0] if focus in le_focus.classes_ else 0
        }
    ])

    prediction = model.predict(input_data)[0]
    server_name = le_server.inverse_transform([prediction])[0]

    st.success(f"Recommended server for you: **{server_name}**: {to_URL[server_name]}")
