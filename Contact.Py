import streamlit as st

# Custom CSS for Social Icons
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .social-container {
            display: flex;
            gap: 20px;
            font-size: 30px;
        }
        .social-icon { color: white; text-decoration: none; transition: 0.3s; }
        .social-icon:hover { color: #1DA1F2; }
    </style>
""", unsafe_allow_html=True)

st.title("📬 Get In Touch")

# Contact Information
st.write(f"📧 **Email:** outreachbyali@gmail.com")
st.write(f"📞 **WhatsApp:** [03119883980](https://wa.me/923119883980)")

# Social Media Icons
st.write("### Follow Us")
st.markdown("""
    <div class="social-container">
        <a href="https://www.facebook.com/AliZa1201" target="_blank" class="social-icon"><i class="fab fa-facebook"></i></a>
        <a href="https://www.instagram.com/ah_physicist?igsh=cHJ1d3o3eWY2eDJs" target="_blank" class="social-icon"><i class="fab fa-instagram"></i></a>
    </div>
""", unsafe_allow_html=True)
