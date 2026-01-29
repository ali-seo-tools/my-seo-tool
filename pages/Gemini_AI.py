import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="AI SEO Expert | Ali SEO Global", layout="wide")

# --- API KEY CONFIGURATION ---
# Paste your API Key inside the quotes below
API_KEY = "AIzaSyDeShr0OPl_kc44UslLFGKR5-ZtIvlQYpk" 

# Initialize Gemini
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("API Configuration Failed. Please check your key.")

# UI Elements
st.title("🤖 Gemini AI SEO Consultant")
st.write("Enter your SEO questions or content requirements below to get instant AI-powered advice.")

st.divider()

# User Input Section
user_query = st.text_area("What would you like to ask?", placeholder="e.g. Write a 500-word blog post about Guest Posting strategies...")

if st.button("Generate Response"):
    if user_query:
        with st.spinner("AI is thinking..."):
            try:
                response = model.generate_content(user_query)
                st.success("Analysis Complete!")
                st.markdown("### AI Output:")
                st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt or question first.")

# Sidebar Info
st.sidebar.info("This tool is powered by Google Gemini Pro. Use it to generate keywords, blog outlines, or SEO audits.")
