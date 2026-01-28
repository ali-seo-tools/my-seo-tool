import streamlit as st
from duckduckgo_search import DDGS

# 1. AI Page Setup
st.set_page_config(page_title="Ali AI SEO Agency", layout="wide", page_icon="🤖")

# Hiding Toolbar for Professional Look
st.markdown("<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;} .stDeployButton {display:none;}</style>", unsafe_allow_html=True)

# --- SIDEBAR ACCESS ---
is_paid = False
with st.sidebar:
    st.title("🛡️ VIP Access")
    if st.query_params.get("admin") == "true":
        st.success("Admin Active")
        is_paid = True
    else:
        status = st.selectbox("Status", ["Unpaid", "Paid"])
        if status == "Paid":
            if st.text_input("Admin Key", type="password") == "ali786":
                is_paid = True
                st.success("Unlocked!")

# --- MAIN AI ENGINE ---
st.title("🤖 Ali AI Vendor Site Finder")

if is_paid:
    niche = st.text_input("Enter Niche (e.g. Fashion, Business, Tech):")
    if st.button("🔍 Find Vendor Sites Now"):
        if niche:
            with st.spinner("AI is scanning live web for Vendors..."):
                try:
                    # Professional AI Search Query
                    query = f"{niche} write for us guest post"
                    
                    with DDGS() as ddgs:
                        # DuckDuckGo search is more stable than Google
                        results = list(ddgs.text(query, max_results=15))
                    
                    if results:
                        st.success(f"AI Found {len(results)} Vendor Sites!")
                        for r in results:
                            st.markdown(f"""
                            <div style="background-color: #f0f2f6; padding: 15px; border-radius: 10px; border-left: 5px solid #1a73e8; margin-bottom: 10px;">
                                <h4 style="margin:0;"><a href="{r['href']}" target="_blank" style="color: #1a73e8; text-decoration: none;">🔗 {r['title']}</a></h4>
                                <p style="color: #555; font-size: 0.9em;">{r.get('body', 'Click link to view site details.')[:200]}</p>
                            </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.warning("No sites found. Try a broader niche like 'Business' or 'Tech'.")
                except Exception as e:
                    st.error("AI is busy. Please wait 10 seconds and try again.")
        else:
            st.warning("Please type a niche name.")
else:
    st.info("🔒 Enter Key in sidebar to unlock.")
