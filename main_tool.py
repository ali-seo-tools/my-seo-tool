import streamlit as st

# 1. LUXURY PAGE SETUP
st.set_page_config(page_title="ALI SEO GLOBAL | #1 Outreach Agency", layout="wide", page_icon="🚀")

# 2. THEME STYLING
st.markdown("""
    <style>
    .stApp { background: #05070a; color: white; }
    .nav-bar {
        display: flex; justify-content: center; gap: 20px; 
        background: rgba(255,255,255,0.05); padding: 15px; 
        border-radius: 50px; margin-bottom: 30px; border: 1px solid #1e293b;
    }
    .hero-box {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(37, 99, 235, 0.05) 100%);
        padding: 60px; border-radius: 30px; text-align: center; border: 1px solid rgba(59, 130, 246, 0.2);
    }
    .feature-card { background: #111827; border: 1px solid #1e293b; padding: 25px; border-radius: 15px; }
    header {visibility: hidden;} footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. TOP NAVIGATION MENU (Ab ye hamesha nazar ayega)
st.markdown('<div class="nav-bar">', unsafe_allow_html=True)
col_nav1, col_nav2, col_nav3, col_nav4, col_nav5 = st.columns(5)
with col_nav1: home_btn = st.button("🏠 Home")
with col_nav2: database_btn = st.button("🔍 Database")
with col_nav3: pricing_btn = st.button("💰 Pricing")
with col_nav4: about_btn = st.button("👤 About")
with col_nav5: contact_btn = st.button("📞 Contact")
st.markdown('</div>', unsafe_allow_html=True)

# 4. PAGE ROUTING (Hamesha Home se shuru hoga)
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

if home_btn: st.session_state.current_page = "Home"
if database_btn: st.session_state.current_page = "Database"
if pricing_btn: st.session_state.current_page = "Pricing"
if about_btn: st.session_state.current_page = "About"
if contact_btn: st.session_state.current_page = "Contact"

# 5. CONTENT ACCORDING TO BUTTONS
if st.session_state.current_page == "Home":
    st.markdown("""
        <div class="hero-box">
            <h1 style="font-size: 50px;">Stop Cold Pitching. Get <span style="color: #3b82f6;">"YES"</span> on Autopilot.</h1>
            <p style="font-size: 20px; color: #94a3b8;">The world's most advanced SEO Guest Posting database for elite agencies.</p>
        </div>
    """, unsafe_allow_html=True)
    st.write("### Why Choose Ali SEO Agency?")
    c1, c2, c3 = st.columns(3)
    c1.markdown('<div class="feature-card"><h3>Verified Leads</h3><p>Direct contacts with 100% reply rate.</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="feature-card"><h3>Live Metrics</h3><p>Real-time DA & Traffic data.</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="feature-card"><h3>AI Outreach</h3><p>Personalized pitches in seconds.</p></div>', unsafe_allow_html=True)

elif st.session_state.current_page == "Database":
    st.title("🎯 Premium Vendor Database")
    key = st.text_input("Enter License Key", type="password")
    if key == "ali786":
        st.success("Authorized! Fetching 5,000+ Premium Vendors...")
    else:
        st.warning("Locked: Enter key 'ali786' to unlock.")

elif st.session_state.current_page == "Pricing":
    st.title("Simple Pricing, Serious Value")
    p1, p2, p3 = st.columns(3)
    p1.markdown('<div class="feature-card"><h3>Starter</h3><h2>$29/mo</h2><p>500 Credits</p></div>', unsafe_allow_html=True)
    p2.markdown('<div class="feature-card" style="border: 2px solid #3b82f6;"><h3>Pro</h3><h2>$69/mo</h2><p>5,000 Credits</p></div>', unsafe_allow_html=True)
    p3.markdown('<div class="feature-card"><h3>Elite</h3><h2>$119/mo</h2><p>Unlimited Access</p></div>', unsafe_allow_html=True)

elif st.session_state.current_page == "Contact":
    st.title("Get In Touch")
    st.markdown(f"""
        <div class="hero-box">
            <h3>Contact Details</h3>
            <p>📧 <b>Email:</b> outreachbyali@gmail.com</p>
            <p>📱 <b>WhatsApp:</b> +92 311 9883980</p>
            <br>
            <a href="https://wa.me/923119883980" style="background:#25d366; color:white; padding:15px 30px; text-decoration:none; border-radius:10px; font-weight:bold;">Chat on WhatsApp</a>
            <div style="margin-top:20px;">
                <a href="https://www.facebook.com/AliZa1201" target="_blank">Facebook</a> | 
                <a href="https://www.instagram.com/ah_physicist" target="_blank">Instagram</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.current_page == "About":
    st.title("Meet Ali")
    st.write("Founder of Ali SEO Global, Specialist in Link Building and High-Authority Outreach.")
