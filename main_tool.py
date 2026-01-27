import streamlit as st
from googlesearch import search

# Page Setting
st.set_page_config(page_title="Ali SEO Agency", page_icon="🚀")

# 1. Secret Admin Access via URL
# If you open: ali-seo-agency.streamlit.app/?admin=true
# The tool will be FREE for you only.
query_params = st.query_params
is_admin = query_params.get("admin") == "true"

# 2. Sidebar for Customers
st.sidebar.header("🔒 Premium Access")

if is_admin:
    st.sidebar.success("Welcome Ali! Admin Mode Active.")
    is_paid = True
else:
    st.sidebar.write("To unlock, pay RS. 2500 via JazzCash:")
    st.sidebar.info("Account: 03119883980")
    
    status = st.sidebar.selectbox("Payment Status", ["Unpaid", "Paid"])
    
    if status == "Paid":
        # Password for customers who have paid
        password = st.sidebar.text_input("Enter Admin Password", type="password")
        if password == "ali786":
            st.sidebar.success("Access Granted!")
            is_paid = True
        else:
            st.sidebar.error("Incorrect Password")
            is_paid = False
    else:
        is_paid = False

# 3. Main App Interface
st.title("🚀 Professional Guest Post Finder")

if is_paid:
    query = st.text_input("What niche/topic are you looking for?")
    if st.button("Search for Leads"):
        if query:
            with st.spinner("Finding high-quality sites..."):
                # Real-time search using Google
                results = search(f"write for us {query}", num_results=15)
                for link in results:
                    st.write(f"✅ Found: {link}")
        else:
            st.warning("Please enter a niche first.")
else:
    st.warning("Tool is Locked. Please pay RS. 2500 and contact Admin for the password.")
