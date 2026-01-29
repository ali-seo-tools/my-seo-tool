import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="AI SEO Consultant", layout="wide")

# Your Provided API Key
API_KEY = "AIzaSyCnIyWGLBTHASU4jsWsRskBPpswtjrLfeM"

# Configure the SDK to use the stable v1 version
genai.configure(api_key=API_KEY)

st.title("🤖 Gemini AI SEO Expert")
st.write("Professional SEO advice instantly.")
st.divider()

user_query = st.text_area("What would you like to ask?", placeholder="e.g., Write a blog outline for SEO...")

if st.button("Generate Response"):
    if user_query:
        with st.spinner("AI is thinking..."):
            try:
                # Using the stable 'gemini-1.5-flash' model
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(user_query)
                
                st.success("Analysis Complete!")
                st.markdown("### AI SEO Response:")
                st.write(response.text)
            except Exception as e:
                # If it fails, it will show a specific error to help us debug
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question first.")

st.sidebar.info("Tool powered by Google Gemini 1.5 Flash.")
