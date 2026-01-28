import streamlit as st

st.set_page_config(page_title="Ali SEO Agency", layout="wide")

# Sidebar
with st.sidebar:
    st.title("🛡️ VIP Access")
    pw = st.text_input("Enter Key", type="password")
    access = (pw == "ali786")

st.title("🤖 Ali AI Instant Vendor Finder")

# --- DATA BASE (Yahan aap jitni chahein sites add kar sakte hain) ---
vendor_data = {
    "Fashion": [
        "https://www.vogue.com/write-for-us",
        "https://www.fashionista.com/guidelines",
        "https://www.elle.com/contact-us",
        "https://www.refinery29.com/en-us/contact-us",
        "https://www.glamour.com/story/contact-us"
    ],
    "Tech": [
        "https://www.techcrunch.com/submit",
        "https://www.wired.com/about/contact",
        "https://www.mashable.com/submit",
        "https://www.theverge.com/contact-us",
        "https://www.zdnet.com/contact"
    ],
    "Business": [
        "https://www.forbes.com/contact",
        "https://www.entrepreneur.com/contact",
        "https://www.inc.com/contact",
        "https://www.businessinsider.com/contact",
        "https://www.fastcompany.com/contact"
    ]
}

if access:
    niche = st.selectbox("Select Niche", ["Fashion", "Tech", "Business"])
    
    if st.button("Show Sites"):
        sites = vendor_data.get(niche, [])
        st.success(f"✅ Found {len(sites)} Verified {niche} Vendors")
        
        for s in sites:
            st.info(f"🔗 {s}")
            st.code(s) # Copy karne ke liye asani
else:
    st.warning("🔒 Enter password to see the list.")
