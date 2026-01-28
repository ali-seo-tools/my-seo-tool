import streamlit as st
import pandas as pd
from datetime import datetime

# 1. GLOBAL CONFIG & SEO
st.set_page_config(page_title="ALI SEO GLOBAL | #1 Guest Posting Agency", layout="wide", page_icon="🌐")

# 2. PROFESSIONAL ULTIMATE UI (Dark & White Mix)
st.markdown("""
    <style>
    /* Premium Background & Text */
    .stApp { background: #0b0e14; color: #ffffff; font-family: 'Inter', sans-serif; }
    
    /* Luxury Navigation */
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    
    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border-radius: 15px; padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #007bff, #00d4ff);
        color: white; border: none; border-radius: 8px;
        font-weight: bold; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 15px rgba(0,123,255,0.5); }
    
    /* Footer & Header Hide */
    header {visibility: hidden;} footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR NAVIGATION & SOCIALS
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #007bff;'>ALI SEO GLOBAL</h1>", unsafe_allow_html=True)
    # Placeholder for Your Photo
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", caption="Ali - Founder & CEO")
    
    menu = st.sidebar.selectbox("Navigate Agency", 
        ["🏠 Home", "🚀 Services", "🔍 Guest Post Provider", "📝 Write For Us", "👤 About Me", "📊 Portfolio", "💰 Pricing", "📞 Contact Us", "⚖️ Privacy & Terms"])
    
    st.divider()
    st.markdown("### **Connect with Founder**")
    st.markdown(f"""
        <a href="https://www.facebook.com/AliZa1201" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" width="30"></a>&nbsp;&nbsp;
        <a href="https://www.instagram.com/ah_physicist?igsh=cHJ1d3o3eWY2eDJs" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" width="30"></a>&nbsp;&nbsp;
        <a href="https://wa.me/923119883980" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" width="30"></a>
    """, unsafe_allow_html=True)

# 4. PAGE LOGIC
if menu == "🏠 Home":
    st.title("🌎 World's #1 Premium Guest Posting Agency")
    st.subheader("We Don't Just Build Links, We Build Authority.")
    
    # CTA Banner
    st.markdown("""
        <div class="glass-card" style="background: linear-gradient(90deg, #007bff22, #00d4ff22);">
            <h2>Rank Your Business on Page 1</h2>
            <p>Get access to 5,000+ High-Traffic Verified Vendors. Start your outreach today.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Client Logos Section
    st.write("---")
    st.caption("TRUSTED BY GLOBAL BRANDS")
    cols = st.columns(5)
    logos = ["Forbes", "TechCrunch", "Wired", "Entrepreneur", "Business Insider"]
    for i, col in enumerate(cols): col.button(logos[i], disabled=True)

elif menu == "🚀 Services":
    st.title("Our Professional SEO Services")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="glass-card"><h3>SEO Audit</h3><p>Deep technical analysis of your domain ranking.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="glass-card"><h3>Guest Posting</h3><p>High DA backlinks from niche-relevant sites.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="glass-card"><h3>Outreach</h3><p>Manual relationship building with site owners.</p></div>', unsafe_allow_html=True)

elif menu == "🔍 Guest Post Provider":
    st.title("🎯 Premium Vendor Database")
    key = st.text_input("Enter License Key", type="password")
    if key == "ali786":
        st.success("Database Unlocked")
        niche = st.selectbox("Select Niche", ["Tech", "Business", "Health", "Fashion"])
        st.info(f"Displaying top {niche} sites with DA 50+...")
        # Data table code goes here
    else:
        st.warning("Enter key 'ali786' to access private vendor list.")

elif menu == "👤 About Me":
    st.title("Personal Branding: Meet Ali")
    col_a, col_b = st.columns([1, 2])
    with col_a:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png") # Replace with your photo link
    with col_b:
        st.markdown("""
            ### Professional SEO Consultant & Physicist
            I bridge the gap between technical data and creative outreach. 
            With a background in analytical thinking and years of SEO experience, 
            I help brands achieve explosive growth through strategic link building.
        """)

elif menu == "💰 Pricing":
    st.title("Flexible Pricing Plans")
    p1, p2, p3 = st.columns(3)
    p1.markdown('<div class="glass-card"><h3>Starter</h3><h1>$99</h1><p>5 Guest Posts<br>DA 30+<br>24/7 Support</p></div>', unsafe_allow_html=True)
    p2.markdown('<div class="glass-card" style="border: 2px solid #007bff;"><h3>Business</h3><h1>$299</h1><p>15 Guest Posts<br>DA 50+<br>SEO Audit</p></div>', unsafe_allow_html=True)
    p3.markdown('<div class="glass-card"><h3>Elite</h3><h1>$599</h1><p>Unlimited Outreach<br>DA 80+<br>Dedicated Manager</p></div>', unsafe_allow_html=True)

elif menu == "📞 Contact Us":
    st.title("Let's Talk Business")
    with st.form("contact_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        msg = st.text_area("How can we help you?")
        if st.form_submit_button("Send Message"):
            st.success("Message Sent! Ali will contact you shortly.")
    
    st.divider()
    st.markdown(f"📧 **Email:** outreachbyali@gmail.com")
    st.markdown(f"📱 **WhatsApp:** [Chat Now](https://wa.me/923119883980)")

elif menu == "📊 Portfolio":
    st.title("Our Proven Results")
    st.image("https://i.imgur.com/8B9Wz6p.png", caption="Ranking Growth of our Latest Client")
    st.markdown('<div class="glass-card">"Ali helped us increase our organic traffic by 400% in just 3 months!" - <b>Global Tech Corp</b></div>', unsafe_allow_html=True)

elif menu == "⚖️ Privacy & Terms":
    st.title("Legal & Privacy")
    st.write("Your data is 100% secure with Ali SEO Global. We follow strict GDPR compliance.")

# 5. GLOBAL FOOTER
st.divider()
f1, f2, f3 = st.columns(3)
f1.write("© 2026 ALI SEO GLOBAL. All Rights Reserved.")
f2.write("Outreach Specialist | Guest Post Provider")
f3.write("Email: outreachbyali@gmail.com")
