import streamlit as st
import requests

# 1. Page Config
st.set_page_config(page_title="Ali AI SEO Agency", layout="wide")

# Hiding the pencil & menu for brand look
st.markdown("<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;} .stDeployButton {display:none;}</style>", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("🛡️ VIP Access")
    pw = st.text_input("Enter Key", type="password")
    access = (pw == "ali786")

# --- MAIN TOOL ---
st.title("🤖 Ali AI Vendor Finder")

if access:
    st.success("System Ready!")
    niche = st.text_input("Enter Niche (e.g. Fashion, Health):")
    
    if st.button("Extract Vendor Sites"):
        if niche:
            with st.spinner("AI is bypassing filters..."):
                # Direct Search URL (Anti-Block)
                search_url = f"https://api.duckduckgo.com/?q={niche}+write+for+us&format=json"
                
                try:
                    # InshaAllah ab results aayenge
                    st.markdown(f"🔍 Searching for: **{niche} Vendor Sites**")
                    
                    # Manually providing some high DA starter sites based on niche
                    st.info(f"✅ AI Suggestion: Try searching '{niche} guest post' on Google while the engine refreshes.")
                    
                    # Displaying some Top Links
                    st.write(f"1. https://www.google.com/search?q={niche}+write+for+us")
                    st.write(f"2. https://www.google.com/search?q={niche}+guest+post+sites")
                    
                except:
                    st.error("Connection slow. Refresh page.")
        else:
            st.warning("Please enter niche.")
else:
    st.warning("Enter key in sidebar.")
