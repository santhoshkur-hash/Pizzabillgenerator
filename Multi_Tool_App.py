import streamlit as st
from google import genai

# 1. Initialize the client
# st.secrets looks for a key named GEMINI_API_KEY.
# On your computer, it finds this in .streamlit/secrets.toml
# On the Cloud, it finds this in the 'Secrets' settings menu.
try:
    client = genai.Client(api_key=st.secrets["AIzaSyDWa0s71Y5JraxRa8zlB5piGHIAR1rIsXw"])
except Exception as e:
    st.error("API Key not found! Make sure you set up your secrets.toml file.")
    st.stop()

st.title("🤖 GenAI Multi-Tool")

# 2. Sidebar menu
choice = st.sidebar.selectbox("Select a tool", ["Email Generator", "Text Summarizer"])

# 3. Application Logic
if choice == "Email Generator":
    st.subheader("Email Generator")
    topic = st.text_input("Enter the topic of the email:")
    tone = st.text_input("Enter the tone (e.g., formal, friendly):")

    if st.button("Generate Email"):
        with st.spinner('Generating...'):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Write a {tone} email about {topic}"
            )
            st.write("--- Generated Email ---")
            st.write(response.text)

elif choice == "Text Summarizer":
    st.subheader("Text Summarizer")
    text = st.text_area("Enter the text you want to summarize:")

    if st.button("Summarize"):
        with st.spinner('Summarizing...'):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Summarize the following text in short bullet points: {text}"
            )
            st.write("--- Summary ---")
            st.write(response.text)