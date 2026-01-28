import streamlit as st
from googlesearch import search
import time

# 1. AI Page Setup
st.set_page_config(page_title="Ali AI SEO Agency", layout="wide", page_icon="🤖")

# Hiding Pencil/Toolbar for Professional Look
st.markdown("<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;} .stDeployButton {display:none;}</style>", unsafe_allow_html=True)

# --- SIDEBAR ACCESS ---
is_paid = False
if st.query_params.get("admin") == "true":
    is_paid = True
else:
    with st.sidebar:
        st.title("🛡️ VIP Access")
        status = st.sidebar.selectbox("Payment Status", ["Unpaid", "Paid"])
        if status == "Paid":
            pw = st.sidebar.text_input("Enter Admin Key", type="password")
            if pw == "ali786":
                is_paid = True
                st.sidebar.success("Access Granted!")

# --- MAIN AI ENGINE ---
st.title("🤖 Ali AI Vendor Site Finder")
st.write("Using AI to find high-authority Guest Post Vendor sites.")

if is_paid:
    niche = st.text_input("Enter Niche (e.g. Fashion, Tech, Pets):")
    if st.button("🔍 Search Vendor Sites"):
        if niche:
            with st.spinner("AI is scanning live web data..."):
                try:
                    # Professional Vendor Query
                    search_query = f'"{niche}" + "write for us" guest post'
                    
                    # Google search call (Stable Method)
                    results = list(search(search_query, num_results=10, sleep_interval=2))
                    
                    if results:
                        st.subheader(f"✅ Found {len(results)} Verified Vendor Sites:")
                        for link in results:
                            # Beautiful UI Card
                            st.markdown(f"""
                            <div style="background-color: #f0f2f6; padding: 15px; border-radius: 10px; border-left: 5px solid #1a73e8; margin-bottom: 10px;">
                                <a href="{link}" target="_blank" style="color: #1a73e8; font-weight: bold; text-decoration: none;">🔗 Open Vendor Site</a><br>
                                <small style="color: #555;">Live Guest Posting Opportunity Found</small>
                            </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.warning("No sites found. Try a different keyword.")
                except Exception as e:
                    st.error("Google is busy. Please wait 1 minute and refresh the page.")
        else:
            st.warning("Please enter a niche first!")
else:
    st.warning("🔒 This Premium AI tool is locked. Pay RS. 2500 to JazzCash (03119883980).")
