import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI SEO Consultant", layout="wide")

st.title("🤖 Gemini AI SEO Expert")
st.write("Get professional SEO advice and content ideas instantly.")

api_key = st.text_input("Enter your Gemini API Key:", type="password")
user_input = st.text_area("What is your SEO question? (e.g., Give me 5 blog ideas for 'Guest Posting')")

if st.button("Ask AI"):
    if api_key and user_input:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(user_input)
            st.success("AI Advice:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter your API key and question.")
