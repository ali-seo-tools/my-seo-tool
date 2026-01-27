import streamlit as st
import csv
from googlesearch import search

# --- WEBSITE CONFIGURATION ---
st.set_page_config(page_title="SEO Agency Tool", layout="wide")
st.title("🚀 Professional Guest Post Finder")

# --- SIDEBAR: JAZZCASH PAYMENT ---
st.sidebar.header("💳 Premium Access")
st.sidebar.write("To unlock, pay **RS. 2500** to JazzCash:")
st.sidebar.info("Account: **03119883980**")

# ADMIN KEY: Select 'Paid' to test
payment_status = st.sidebar.selectbox("Payment Status", ["Unpaid", "Paid"])

# --- MAIN INTERFACE ---
query = st.text_input("What niche are you looking for?")

if st.button("Find Leads Now"):
    if payment_status == "Unpaid":
        st.error("❌ Please pay via JazzCash to see results.")
    else:
        st.success(f"🔍 Searching Google for: {query}")
        for url in search(query, num_results=5):
            st.write(f"🔗 Found: {url}")