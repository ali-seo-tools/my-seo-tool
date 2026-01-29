import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm

# Page Configuration
st.set_page_config(page_title="AI SEO Consultant", layout="wide")

# Your API Key
API_KEY = "AIzaSyCnlyWGLBTHASU4jsWsRskBPpswtjrLfeM"

# FORCE STABLE CONFIGURATION
genai.configure(api_key=API_KEY)

st.title("🤖 Gemini AI SEO Expert")
st.write("Professional SEO advice instantly.")
st.divider()

user_query = st.text_area("What is your SEO question?", placeholder="Ask anything...")

if st.button("Generate Response"):
    if user_query:
        with st.spinner("AI is thinking..."):
            try:
                # We use the newest stable model name
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # We call the generation
                response = model.generate_content(user_query)
                
                st.success("Analysis Complete!")
                st.markdown("### AI SEO Response:")
                st.write(response.text)
            except Exception as e:
                # If it still fails, we show the exact technical error
                st.error(f"Technical Error: {e}")
    else:
        st.warning("Please enter a question first.")

st.sidebar.info("Stable Version 1.5 Flash Active.")
