import streamlit as st

# 1. LUXURY PAGE SETUP
st.set_page_config(page_title="ALI SEO GLOBAL | #1 Outreach Agency", layout="wide", page_icon="🚀")

# 2. THE ULTIMATE STYLING (OutreachFlow Style)
st.markdown(f"""
    <style>
    /* Dark Premium Theme */
    .stApp {{ background: #05070a; color: white; font-family: 'Inter', sans-serif; }}
    
    /* Navigation Glass Effect */
    [data-testid="stSidebar"] {{ background-color: #0b0e14; border-right: 1px solid #1e293b; }}
    
    /* Hero Section Card */
    .hero-box {{
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(37, 99, 235, 0.05) 100%);
        padding: 60px; border-radius: 30px; text-align: center; border: 1px solid rgba(59, 130, 246, 0.2);
        margin-bottom: 40px;
    }}
    
    /* Pricing & Feature Cards */
    .feature-card {{
        background: #111827; border: 1px solid #1e293b; padding: 25px; border-radius: 15px; 
        transition: 0.3s; height: 100%;
    }}
    .feature-card:hover {{ border-color: #3b82f6; transform: translateY(-5px); }}
    
    .price-btn {{
        background: #3b82f6; color: white; padding: 10px 20px; border-radius: 8px;
        text-decoration: none; font-weight: bold; display: block; text-align: center; margin-top: 15px;
    }}
    
    header {{visibility: hidden;}} footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# 3. NAVIGATION DROPDOWN (Pages)
with st.sidebar:
    st.markdown("<h1 style='color: #3b82f6;'>ALI AGENCY</h1>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100) # Founder Photo
    
    page = st.selectbox("Menu", ["🏠 Home", "🚀 Services", "🔍 Guest Post Database", "👤 About Founder", "📞 Contact & Icons", "💰 Pricing Plans", "❓ FAQs"])
    
    st.divider()
    # SOCIAL ICONS
    st.markdown(f"""
        <div style="display: flex; gap: 15px; justify-content: center;">
            <a href="https://www.facebook.com/AliZa1201" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" width="30"></a>
            <a href="https://www.instagram.com/ah_physicist" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" width="30"></a>
            <a href="https://wa.me/923119883980" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" width="30"></a>
        </div>
    """, unsafe_allow_html=True)

# 4. PAGES CONTENT
if page == "🏠 Home":
    st.markdown("""
        <div class="hero-box">
            <h1 style="font-size: 50px; margin-bottom: 10px;">Stop Cold Pitching. Get <span style="color: #3b82f6;">"YES"</span> on Autopilot.</h1>
            <p style="font-size: 20px; color: #94a3b8;">The world's most advanced SEO Guest Posting database for elite agencies.</p>
            <br><a href="#" class="price-btn" style="width: 200px; margin: 0 auto;">Get Started Now</a>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("### Why Choose Ali SEO Agency?")
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div class="feature-card"><h3>Verified Leads</h3><p>Direct contacts of site owners with 100% reply rate.</p></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="feature-card"><h3>Live SEO Metrics</h3><p>Real-time DA, DR, and Traffic data from Ahrefs.</p></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="feature-card"><h3>AI Outreach</h3><p>Our AI writes personalized pitches for your campaign.</p></div>', unsafe_allow_html=True)

elif page == "🔍 Guest Post Database":
    st.title("🎯 Premium Vendor Database")
    key = st.text_input("Enter License Key", type="password")
    if key == "ali786":
        st.success("Authorized! Fetching 5,000+ Premium Vendors...")
        st.selectbox("Niche", ["Technology", "Business", "Health", "Real Estate"])
        st.button("Extract Data")
    else:
        st.warning("Please enter your premium license key in the sidebar.")

elif page == "💰 Pricing Plans":
    st.title("Simple Pricing, Serious Value")
    p1, p2, p3 = st.columns(3)
    with p1: st.markdown('<div class="feature-card"><h3>Starter</h3><h2>$29/mo</h2><p>500 Credits<br>Basic Support</p></div>', unsafe_allow_html=True)
    with p2: st.markdown('<div class="feature-card" style="border: 2px solid #3b82f6;"><h3>Pro</h3><h2>$69/mo</h2><p>5000 Credits<br>Priority Support</p></div>', unsafe_allow_html=True)
    with p3: st.markdown('<div class="feature-card"><h3>Elite</h3><h2>$119/mo</h2><p>Unlimited<br>Dedicated Manager</p></div>', unsafe_allow_html=True)

elif page == "📞 Contact & Icons":
    st.title("Get In Touch")
    st.markdown(f"""
        <div class="hero-box">
            <h3>Direct Contact</h3>
            <p>📧 <b>Email:</b> outreachbyali@gmail.com</p>
            <p>📱 <b>WhatsApp:</b> +92 311 9883980</p>
            <hr>
            <h4>Find me on Social Media</h4>
            <a href="https://wa.me/923119883980" class="price-btn">Chat on WhatsApp</a>
        </div>
    """, unsafe_allow_html=True)

elif page == "👤 About Founder":
    st.title("About Ali")
    st.markdown('<div class="glass-card"><h3>Founder & SEO Specialist</h3><p>Hi! I am Ali, an AH Physicist and SEO Outreach specialist. I built this tool to help agencies scale their link-building without the headache of manual scraping.</p></div>', unsafe_allow_html=True)

elif page == "❓ FAQs":
    st.title("Common Questions")
    with st.expander("How do credits work?"): st.write("Each site extraction costs 1 credit.")
    with st.expander("Can I bring my own SMTP?"): st.write("Yes, our Pro and Elite plans support custom SMTP.")
