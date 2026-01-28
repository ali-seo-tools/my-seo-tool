import streamlit as st

# Page Title
st.set_page_config(page_title="Ali SEO Agency", layout="wide")

# Hide Toolbar
st.markdown("<style>header {visibility: hidden;} footer {visibility: hidden;}</style>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🛡️ Admin Panel")
    pw = st.text_input("Enter Key", type="password")
    access = (pw == "ali786")

st.title("🚀 Ali AI Premium Vendor Database")

# --- MASTER DATABASE (Ye hamesha chalega) ---
database = {
    "Fashion": [
        "https://www.vogue.com/write-for-us",
        "https://www.fashionista.com/guidelines",
        "https://www.elle.com/contact-us",
        "https://www.glamour.com/story/contact-us",
        "https://www.refinery29.com/en-us/contact-us",
        "https://www.harpersbazaar.com/about/a2695/contact-us/",
        "https://www.thefashionspot.com/contact/",
        "https://www.whowhatwear.com/about-us"
    ],
    "Tech": [
        "https://www.techcrunch.com/submit",
        "https://www.wired.com/about/contact",
        "https://www.mashable.com/submit",
        "https://www.theverge.com/contact-us",
        "https://www.zdnet.com/contact",
        "https://www.cnet.com/contact/",
        "https://www.gizmodo.com/about",
        "https://www.digitaltrends.com/contact/"
    ],
    "Business": [
        "https://www.forbes.com/contact",
        "https://www.entrepreneur.com/contact",
        "https://www.inc.com/contact",
        "https://www.businessinsider.com/contact",
        "https://www.fastcompany.com/contact",
        "https://www.hbr.org/contact",
        "https://www.economist.com/contact-us",
        "https://www.bloomberg.com/feedback"
    ]
}

if access:
    st.success("✅ Database Unlocked")
    niche = st.selectbox("Apni Niche Select Karein:", ["Fashion", "Tech", "Business"])
    
    if st.button("Sites Dekhein"):
        sites = database.get(niche, [])
        st.subheader(f"📍 Verified {niche} Vendors:")
        
        for s in sites:
            st.info(f"🔗 {s}")
            st.code(s) # Is par click karke aap copy kar sakte hain
else:
    st.warning("🔒 Sidebar mein password (ali786) likhein.")
