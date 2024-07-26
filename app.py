# Install Streamlit and pyngrok
!pip install streamlit
!pip install pyngrok

# Set up ngrok auth token (replace 'YOUR_ACTUAL_NGROK_AUTH_TOKEN' with your actual token)
!ngrok authtoken YOUR_ACTUAL_NGROK_AUTH_TOKEN

# Write the Streamlit app to a file
%%writefile app.py
import streamlit as st
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

st.title('Random Password Generator')

length = st.number_input('Enter the desired password length:', min_value=1, max_value=100, value=12)

if st.button('Generate Password'):
    password = generate_password(length)
    st.write(f'Generated Password: `{password}`')

# Run the Streamlit app and expose it using ngrok
import os
from pyngrok import ngrok

# Terminate any existing ngrok tunnels
ngrok.kill()

# Start ngrok
public_url = ngrok.connect(port='8501')
print(f'Public URL: {public_url}')

# Run Streamlit app
os.system('streamlit run app.py &')

