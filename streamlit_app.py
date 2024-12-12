import streamlit as st
import subprocess

def run_flask_app():
    cmd = ["python", "app.py"]
    process = subprocess.Popen(cmd)

st.title("Mijn Website")
st.write("Gebruik de navigatiebalk om door de site te bladeren.")

# Start the Flask app
run_flask_app()

# Embedding the Flask app inside Streamlit
st.write(
    f'<iframe src="http://localhost:5000/" width="100%" height="600"></iframe>',
    unsafe_allow_html=True
)
