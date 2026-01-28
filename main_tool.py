import streamlit as st
from googlesearch import search
import time

# 1. Page Config
st.set_page_config(page_title="Ali AI Vendor Scraper", layout="wide")

# Toolbar Chupane ka Code
st.markdown("<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;} .stDeployButton {display:none;}</style>", unsafe_allow_html=True)

# --- SIDEBAR ACCESS ---
with st.sidebar:
    st.title("🛡️ VIP Control")
    pw = st.text_input("Enter Admin Password", type="password")
    access = (pw == "ali786")

# --- MAIN ENGINE ---
st.title("🤖 Ali AI Auto-Vendor List")
st.write("Enter your niche, and the AI will scrape a list of vendor sites directly below.")

if access:
    niche = st.text_input("Enter Niche (e.g. Fashion, Tech, Business):")
    
    if st.button("Extract List Now"):
        if niche:
            with st.spinner(f"Scraping {niche} Vendor Sites... Please wait..."):
                try:
                    # Advanced Search Query
                    query = f'"{niche}" + "write for us"'
                    
                    # Google se data khinchne ka tareeka
                    # Humne pause 2.0 rakha hai taake Google block na kare
                    results = search(query, num_results=15, sleep_interval=2)
                    
                    st.success(f"✅ Found Vendor Sites for {niche}:")
                    st.markdown("---")
                    
                    # Aik aik kar ke results screen par show karna
                    for i, link in enumerate(results, 1):
                        st.markdown(f"**{i}.** {link}")
                        # Copy button ki sahulat ke liye text input
                        st.code(link) 
                    
                except Exception as e:
                    st.error("Google has temporarily blocked the auto-scraper. Please wait 5 minutes or use the direct search link.")
        else:
            st.warning("Please enter a niche.")
else:
    st.warning("🔒 Please enter the correct password in the sidebar.")
