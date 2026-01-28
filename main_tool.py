import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Page Setup
st.set_page_config(page_title="Ali SEO Pro - VIP", layout="wide", page_icon="💎")

# Professional CSS
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .stMetric { background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .vendor-card { background-color: white; padding: 20px; border-radius: 12px; border-left: 6px solid #007bff; margin-bottom: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    header {visibility: hidden;} footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar License System
with st.sidebar:
    st.title("🛡️ Admin Console")
    access_key = st.text_input("Enter License Key", type="password")
    is_verified = (access_key == "ali786")
    if is_verified:
        st.success("Premium License Verified")
        st.write(f"Logged in: {datetime.now().strftime('%H:%M:%S')}")

# 3. Advanced Database with SEO Metrics
# format: [URL, DA, Traffic, Price]
raw_data = {
    "Technology": [
        ["https://techcrunch.com", "92", "15M", "Contact for Quote"],
        ["https://wired.com", "93", "20M", "$1500+"],
        ["https://thenextweb.com", "89", "2M", "$500"],
        ["https://mashable.com", "91", "10M", "$800"]
    ],
    "Health": [
        ["https://healthline.com", "92", "50M", "High Authority"],
        ["https://medicalnewstoday.com", "91", "30M", "Verified"],
        ["https://psychologytoday.com", "91", "25M", "$400"]
    ],
    "Marketing": [
        ["https://hubspot.com", "92", "10M", "Guest Post Only"],
        ["https://neilpatel.com", "88", "5M", "$600"],
        ["https://searchenginejournal.com", "89", "3M", "$450"]
    ]
}

# 4. Main Interface
if is_verified:
    st.title("🎯 Ali Pro SEO - Vendor Intelligence")
    
    # Top Stats Row
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Vendors", "5,000+")
    c2.metric("Active Leads", "1,240")
    c3.metric("System Status", "Online 100%")

    st.divider()

    # Search Filters
    col_a, col_b = st.columns([2, 1])
    with col_a:
        niche = st.selectbox("Select Target Industry", list(raw_data.keys()))
    with col_b:
        search = st.text_input("Quick Filter (Leave blank to see all)")

    if st.button("🔥 Fetch Premium Leads"):
        leads = raw_data.get(niche, [])
        if search:
            leads = [l for l in leads if search.lower() in l[0].lower()]
        
        st.subheader(f"Results for {niche}")
        
        for l in leads:
            st.markdown(f"""
            <div class="vendor-card">
                <div style="display: flex; justify-content: space-between;">
                    <h3 style="margin:0; color:#007bff;">🌐 {l[0].replace('https://','').upper()}</h3>
                    <span style="background:#e1f5fe; padding:5px 10px; border-radius:15px; font-weight:bold; color:#01579b;">DA: {l[1]}</span>
                </div>
                <p style="margin:10px 0; color:#555;">Monthly Traffic: <b>{l[2]}</b> | Price Status: <b>{l[3]}</b></p>
                <a href="{l[0]}" target="_blank" style="background:#007bff; color:white; padding:8px 15px; text-decoration:none; border-radius:5px; font-size:14px;">Open Site</a>
            </div>
            """, unsafe_allow_html=True)
            st.code(f"Site: {l[0]} | DA: {l[1]}")

    st.divider()
    st.write("📥 **Bulk Actions**")
    st.download_button("Export Lead List", "Site,DA,Traffic\n" + "\n".join([f"{x[0]},{x[1]},{x[2]}" for x in raw_data[niche]]), "seo_leads.csv")

else:
    st.warning("Please verify your license key in the sidebar.")
