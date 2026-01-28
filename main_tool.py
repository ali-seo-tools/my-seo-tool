import streamlit as st
from googlesearch import search

# Page Configuration
st.set_page_config(page_title="Ali SEO Agency", layout="wide")

# Sidebar for Password
with st.sidebar:
    st.title("🔑 VIP Access")
    pw = st.text_input("Enter Admin Password", type="password")
    if pw == "ali786":
        st.success("Unlocked!")
        access = True
    else:
        access = False

# Main App
st.title("🚀 Ali AI Vendor Finder")

if access:
    niche = st.text_input("Enter Niche (e.g. Fashion, Business):")
    if st.button("Search Vendor Sites"):
        if niche:
            with st.spinner("Searching Google..."):
                try:
                    # Simple search query
                    query = f"{niche} write for us"
                    results = list(search(query, num_results=10))
                    
                    if results:
                        for link in results:
                            st.info(f"🔗 {link}")
                    else:
                        st.warning("No results found.")
                except Exception as e:
                    st.error("Too many searches. Please wait 2 minutes.")
        else:
            st.warning("Enter a niche name first.")
else:
    st.warning("Please enter password in sidebar to use the tool.")
