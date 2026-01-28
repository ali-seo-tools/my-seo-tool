import streamlit as st
from duckduckgo_search import DDGS

# 1. Page Config (Python Logic)
st.set_page_config(page_title="Ali AI Vendor", layout="wide")

# Hide Toolbar
st.markdown("<style>header {visibility: hidden;} footer {visibility: hidden;}</style>", unsafe_allow_html=True)

# 2. Sidebar Access
with st.sidebar:
    st.title("🛡️ Admin Panel")
    pw = st.text_input("Enter Key", type="password")
    access = (pw == "ali786")

# 3. Main Logic
st.title("🤖 Python AI Vendor Scraper")

if access:
    niche = st.text_input("Enter Niche (e.g. Health, Fashion):")
    if st.button("Start Extraction"):
        if niche:
            with st.spinner("Python Engine is Scraping..."):
                try:
                    # Search Query
                    query = f'"{niche}" + "write for us"'
                    with DDGS() as ddgs:
                        # Fetching results
                        results = list(ddgs.text(query, max_results=10))
                    
                    if results:
                        st.success(f"Found {len(results)} Sites!")
                        for r in results:
                            # Displaying each link in a card
                            st.markdown(f"✅ **{r['title']}**")
                            st.code(r['href'])
                            st.markdown("---")
                    else:
                        st.warning("No sites found in this niche.")
                except Exception as e:
                    st.error("Engine busy. Wait 15 seconds.")
else:
    st.warning("🔒 Enter password to unlock.")
