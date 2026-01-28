import streamlit as st
from duckduckgo_search import DDGS

# 1. Page Config
st.set_page_config(page_title="Ali AI SEO Agency", layout="wide")

# Hiding Menu/Toolbar
st.markdown("<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;} .stDeployButton {display:none;}</style>", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("🔑 VIP Access")
    pw = st.text_input("Enter Password", type="password")
    access = (pw == "ali786")

# --- MAIN TOOL ---
st.title("🚀 Ali AI Vendor Finder")

if access:
    st.success("Unlocked! Ready to find leads.")
    niche = st.text_input("Enter Niche (e.g. Fashion, Tech):")
    if st.button("Search Vendor Sites"):
        if niche:
            with st.spinner("AI is searching..."):
                try:
                    # Professional Vendor Query
                    query = f"{niche} write for us"
                    with DDGS() as ddgs:
                        results = list(ddgs.text(query, max_results=10))
                    
                    if results:
                        for r in results:
                            st.info(f"🔗 {r['title']}\n{r['href']}")
                    else:
                        st.warning("No sites found. Try again.")
                except Exception as e:
                    st.error("Engine busy. Please wait 10 seconds.")
        else:
            st.warning("Enter a niche first.")
else:
    st.warning("Enter password in sidebar to start.")
