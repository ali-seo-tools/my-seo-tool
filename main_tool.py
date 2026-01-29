import streamlit as st
import google.generativeai as genai

# 1. PAGE SETUP (Professional Look)
st.set_page_config(page_title="Ali SEO GLOBAL", layout="wide", page_icon="🚀")

# Gemini Setup (Yahan apni key lagayen)
genai.configure(api_key="APKI_GEMINI_KEY_YAHAN_LIKHEIN")

# 2. CUSTOM CSS (Design behtar karne ke liye)
st.markdown("""
<style>
    .stApp { background: #05070a; color: white; }
    .price-card {
        padding: 20px;
        border-radius: 15px;
        background: #111827;
        border: 1px solid #1e293b;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# 3. HEADER
st.title("🚀 Ali SEO GLOBAL | #1 Outreach Agency")
st.write("Stop Cold Pitching. Get 'YES' on Autopilot.")

# 4. AI SEO ASSISTANT (Gemini Connection)
st.divider()
st.header("🤖 Gemini AI SEO Expert")
user_input = st.text_input("SEO ke baare mein kuch bhi poochein:")
if user_input:
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_input)
    st.info(response.text)

# 5. EARNING SECTION (Price Table)
st.divider()
st.header("💰 Premium SEO Services ($100 Target)")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="price-card"><h3>Basic</h3><p>5 Guest Posts</p><h2>$20</h2></div>', unsafe_allow_html=True)
    if st.button("Order Basic"):
        st.write("WhatsApp: +923XXXXXXXXX")

with col2:
    st.markdown('<div class="price-card"><h3>Pro</h3><p>AI SEO Audit</p><h2>$50</h2></div>', unsafe_allow_html=True)
    if st.button("Order Pro"):
        st.write("WhatsApp: +923XXXXXXXXX")

with col3:
    st.markdown('<div class="price-card"><h3>Elite</h3><p>Monthly SEO</p><h2>$100</h2></div>', unsafe_allow_html=True)
    if st.button("Order Elite"):
        st.write("WhatsApp: +923XXXXXXXXX")

# 6. ADSENSE & LEGAL PAGES
st.divider()
st.sidebar.title("Navigation")
st.sidebar.write("🏠 Home")
st.sidebar.write("📄 Privacy Policy (AdSense Required)")
st.sidebar.write("📧 Contact Us")
