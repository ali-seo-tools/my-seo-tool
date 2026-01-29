import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="AI SEO Consultant", layout="wide")

# Your API Key
API_KEY = "AIzaSyCnlyWGLBTHASU4jsWsRskBPpswtjrLfeM"

# Setup configuration
genai.configure(api_key=API_KEY)

st.title("🤖 Gemini AI SEO Expert")
st.write("Professional SEO advice instantly.")
st.divider()

user_query = st.text_area("What is your SEO question?", placeholder="e.g., Write 5 keywords for a tech blog...")

if st.button("Generate Response"):
    if user_query:
        with st.spinner("AI is thinking..."):
            try:
                # TRANSPORT='REST' is the key fix for the 404/v1beta error
                model = genai.GenerativeModel(model_name='gemini-1.5-flash')
                response = model.generate_content(user_query, transport='rest')
                
                st.success("Analysis Complete!")
                st.markdown("### AI SEO Response:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Technical Detail: {e}")
                st.info("If you see an 'API Key' error, please wait 5 minutes for Google to activate it.")
    else:
        st.warning("Please enter a question first.")

st.sidebar.markdown("---")
st.sidebar.write("System Status: **Running**")
