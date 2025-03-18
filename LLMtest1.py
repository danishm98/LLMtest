import streamlit as st
import pandas as pd
from transformers import pipeline

# Initialize the text generation pipeline
generator = pipeline('text-generation', model='gpt-3.5-turbo')

# Title of the app
st.title("Ask Questions About Your Excel Data")

# File uploader
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    # Read the uploaded Excel file
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.write("Data from the uploaded file:")
    st.write(df)

    # Convert DataFrame to a string for context
    data_str = df.to_string()

    # User input
    user_input = st.text_input("Type your question here:")

    # Generate response
    if user_input:
        prompt = f"Here is the data:\n{data_str}\n\nQuestion: {user_input}\nAnswer:"
        response = generator(prompt, max_length=100, num_return_sequences=1)
        st.write(response[0]['generated_text'])
