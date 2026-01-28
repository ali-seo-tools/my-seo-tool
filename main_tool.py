import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Advanced Page Configuration
st.set_page_config(
    page_title="Ali SEO Pro - Vendor Finder",
    page_icon="🎯",
    layout="wide"
)

# Professional UI Styling (Outreachflow Style)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    .vendor-card { background-color: white; padding: 20px; border-radius: 10px; border: 1px solid #e1e4e8; margin-bottom: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); }
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar with Access Control & Stats
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1055/1055644.png", width=80)
    st.title("Ali SEO Agency")
    st.info(f"📅 Date: {datetime.now().strftime('%Y-%m-%d')}")
    access_key = st.text_input("License Key", type="password")
    is_verified = (access_key == "ali786")
    
    if is_verified:
        st.success("✅ License: Premium Active")
    else:
        st.error("❌ System Locked")

# 3. Professional Database (Expanded)
vendor_db = {
    "Technology": ["https://techcrunch.com/submit", "https://wired.com/contact", "https://mashable.com/submit", "https://theverge.com/contact"],
    "Fashion": ["https://vogue.com/write-for-us", "https://fashionista.com/guidelines", "https://elle.com/contact", "https://glamour.com/contact"],
    "Business": ["https://forbes.com/contact", "https://entrepreneur.com/contact", "https://inc.com/contact", "https://hbr.org/contact"],
    "Health": ["https://healthline.com", "https://webmd.com", "https://medicalnewstoday.com"],
    "Finance": ["https://investopedia.com", "https://bloomberg.com", "https://marketwatch.com"],
    "Real Estate": ["https://zillow.com/blog", "https://realtor.com/news", "https://biggerpockets.com"],
    "Travel": ["https://lonelyplanet.com", "https://nomadicmatt.com", "https://travelandleisure.com"],
    "Crypto": ["https://coindesk.com", "https://cointelegraph.com", "https://decrypt.co"]
}

# 4. Main Dashboard UI
if is_verified:
    st.title("🎯 Premium Guest Post Vendor Finder")
    st.write("Extract verified high-authority websites for your SEO outreach campaigns.")
    
    # Feature: Multi-Filter Search
    col1, col2 = st.columns([2, 1])
    with col1:
        niche = st.selectbox("Select Target Industry", list(vendor_db.keys()))
    with col2:
        search_query = st.text_input("Filter by Keyword")

    if st.button("Generate Vendor Leads"):
        sites = vendor_db.get(niche, [])
        
        # Filtering logic
        if search_query:
            sites = [s for s in sites if search_query.lower() in s.lower()]
            
        st.subheader(f"📊 Results: {len(sites)} Vendors Found")
        
        # Displaying results in a clean grid
        for site in sites:
            st.markdown(f"""
                <div class="vendor-card">
                    <h4 style="color: #007bff; margin-bottom: 5px;">🌐 {site.split('//')[1].split('/')[0].upper()}</h4>
                    <p style="color: #6c757d; font-size: 0.9em;">Verified Vendor Link</p>
                    <a href="{site}" target="_blank" style="color: #28a745; font-weight: bold;">View Submission Page</a>
                </div>
            """, unsafe_allow_html=True)
            st.code(site) # Feature: Easy Copy for Outreach

    # Feature: Download Capability
    st.divider()
    st.write("📥 **Export Leads:** You can download the current view as a CSV for your team.")
    if st.button("Export to Excel (CSV)"):
        st.download_button("Click to Download", "Site\n" + "\n".join(vendor_db[niche]), "leads.csv")

else:
    st.warning("Please enter your License Key in the sidebar to access the AI Database.")
    st.image("https://i.imgur.com/71S3C0W.png") # Placeholder for professional locked screen
