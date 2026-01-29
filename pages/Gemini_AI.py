import streamlit as st
import google.generativeai as genai

# Simple Setup
st.set_page_config(page_title="AI SEO Tool")
API_KEY = "AIzaSyCnlyWGLBTHASU4jsWsRskBPpswtjrLfeM"

try:
    genai.configure(api_key=API_KEY)
    # Using the 'gemini-pro' name as it's the most stable across all versions
    model = genai.GenerativeModel('gemini-pro')
except:
    st.error("Connection Error")

st.title("🤖 SEO AI Assistant")

user_query = st.text_input("Ask any SEO question:")

if st.button("Get Answer"):
    if user_query:
        try:
            response = model.generate_content(user_query)
            st.success("AI Response:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.info("Please type a question.")
