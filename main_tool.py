import streamlit as st
from googlesearch import search

# 1. Page Config
st.set_page_config(page_title="Ali AI SEO Agency", layout="wide")

# Hiding the toolbar for professional look
st.markdown("<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;} .stDeployButton {display:none;}</style>", unsafe_allow_html=True)

# --- SIDEBAR ACCESS ---
is_paid = False
with st.sidebar:
    st.title("🛡️ VIP Access")
    status = st.selectbox("Status", ["Unpaid", "Paid"])
    if status == "Paid":
        if st.text_input("Admin Key", type="password") == "ali786":
            is_paid = True
            st.success("Unlocked!")

# --- MAIN TOOL ---
st.title("🤖 Ali AI Vendor Finder")

if is_paid:
    niche = st.text_input("Enter Niche (e.g. Fashion, Business):")
    if st.button("Find Vendor Sites Now"):
        if niche:
            with st.spinner("Scanning Google..."):
                try:
                    # Professional Query for Vendors
                    query = f'"{niche}" + "write for us"'
                    
                    # Stable Search Method
                    results = list(search(query, num_results=10))
                    
                    if results:
                        st.success(f"Found {len(results)} Sites!")
                        for link in results:
                            st.markdown(f"""
                            <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 5px solid #007bff; margin-bottom: 10px;">
                                <a href="{link}" target="_blank" style="color: #007bff; font-weight: bold; text-decoration: none;">🔗 Open Site</a>
                            </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.warning("No sites found. Try a different word.")
                except Exception as e:
                    st.error("Too many searches. Please wait 1 minute and refresh.")
        else:
            st.warning("Enter a niche first!")
else:
    st.info("🔒 Enter Key in sidebar to start.")
