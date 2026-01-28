import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Ali SEO Agency | Premium Guest Posting", layout="wide", page_icon="👑")

# Professional Agency UI (Wallpaper & Glass Effects)
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(-45deg, #0f172a, #1e293b, #0f172a);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: white;
    }}
    @keyframes gradient {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    .glass-card {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 25px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }}
    .social-icon {{
        font-size: 30px; margin-right: 20px; text-decoration: none; color: #3b82f6;
    }}
    header {{visibility: hidden;}} footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar Navigation
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #3b82f6;'>ALI AGENCY</h1>", unsafe_allow_html=True)
    st.divider()
    menu = st.radio("Explore Website", ["🏠 Agency Home", "🔍 Vendor Database", "👤 About Me", "📞 Contact & Support"])
    st.divider()
    st.markdown("### **Follow Me**")
    st.markdown(f"""
        <a href="https://www.facebook.com/AliZa1201" target="_blank">🔵 Facebook</a><br>
        <a href="https://www.instagram.com/ah_physicist?igsh=cHJ1d3o3eWY2eDJs" target="_blank">🟣 Instagram</a>
    """, unsafe_allow_html=True)

# 3. Pages Logic
if menu == "🏠 Agency Home":
    st.title("🚀 Premium SEO Guest Posting Services")
    st.markdown("""
    <div class="glass-card">
        <h2>Expert Link Building & Outreach</h2>
        <p>Welcome to Ali SEO Agency. I specialize in providing high-authority, 
        organic traffic backlinks that skyrocket your Google rankings.</p>
        <hr style="border: 0.1px solid rgba(255,255,255,0.1);">
        <p>⭐ <b>100% Indexing Guarantee</b> | ⭐ <b>DA 50-90+ Sites</b> | ⭐ <b>Permanent Do-Follow Links</b></p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "🔍 Vendor Database":
    st.title("🎯 Exclusive Vendor Intelligence")
    pw = st.text_input("Enter License Key", type="password")
    if pw == "ali786":
        st.success("Access Granted. Explore our verified 2026 database.")
        # Database code yahan add hoga (Tech, Fashion etc.)
    else:
        st.warning("Locked: This section is for Premium Clients only.")

elif menu == "👤 About Me":
    st.title("About the Founder")
    st.markdown("""
    <div class="glass-card">
        <h3>Hi, I'm Ali</h3>
        <p>I am a Professional SEO Consultant and outreach expert. My goal is to bridge the gap 
        between high-quality vendors and businesses looking for growth.</p>
        <p>With a deep understanding of <b>Search Engine Algorithms</b>, I ensure that every 
        link you get from my database provides maximum 'Link Juice' to your domain.</p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "📞 Contact & Support":
    st.title("Get In Touch")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        <div class="glass-card">
            <h4>Contact Details</h4>
            <p>📧 <b>Gmail:</b> outreachbyali@gmail.com</p>
            <p>📱 <b>WhatsApp:</b> +92 311 9883980</p>
            <p>📍 <b>Office:</b> Punjab, Pakistan</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.write("Need bulk guest posts? Let's discuss your project on WhatsApp.")
        st.markdown(f'<a href="https://wa.me/923119883980" target="_blank"><button style="background-color: #25d366; color: white; border: none; padding: 15px 30px; border-radius: 10px; cursor: pointer; font-weight: bold; width: 100%;">Chat on WhatsApp</button></a>', unsafe_allow_html=True)
