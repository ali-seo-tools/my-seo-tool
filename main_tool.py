import streamlit as st

st.set_page_config(page_title="Ali SEO Global", layout="wide", page_icon="📈")

# Header Section
st.title("Ali SEO Global")
st.subheader("Dominating Search Engines with AI-Powered SEO")
st.markdown("""
Welcome to the future of digital growth. We combine **Human Expertise** with **Gemini AI** to rank your website on the first page of Google.
""")

st.divider()

# Value Proposition
col1, col2, col3 = st.columns(3)
with col1:
    st.write("### 🤖 AI-Driven")
    st.write("Real-time SEO audits using Google's Gemini Pro.")
with col2:
    st.write("### 🔗 Authority Backlinks")
    st.write("High-quality Guest Posts from DA 50+ websites.")
with col3:
    st.write("### 📈 Data Focused")
    st.write("Metric-based strategies to increase your organic traffic.")

st.sidebar.success("Select a service above to get started.")
