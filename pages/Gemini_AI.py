import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI SEO Consultant", layout="wide")

# Replace this with your actual key (e.g., "AIzaSy...")
API_KEY = "AIzaSyCN9MK1CV9gql-Ih2Lbb3HgEusyFpa8UKA" 

# Correct Setup for 2026
try:
    genai.configure(api_key=API_KEY)
    # Using 'gemini-1.5-flash' which is the fastest and most compatible
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Config Error")

st.title("🤖 Gemini AI SEO Expert")
st.write("Professional SEO advice instantly.")

user_query = st.text_area("Ask your SEO question:")

if st.button("Generate Response"):
    if user_query:
        with st.spinner("AI is thinking..."):
            try:
                # Standard generation
                response = model.generate_content(user_query)
                st.success("Analysis Complete!")
                st.write(response.text)
            except Exception as e:
                # If this fails, it's either the key or the model name
                st.error(f"Error: {e}")
                st.info("Try changing 'gemini-1.5-flash' to 'gemini-1.5-pro' in the code if this persists.")
    else:
        st.warning("Please enter a question.")
