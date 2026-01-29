import streamlit as st

st.set_page_config(page_title="Contact | Ali SEO Global", layout="wide")

st.title("📬 Contact Ali SEO Global")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Reach Out Directly")
    st.write("📧 **Email:** outreachbyali@gmail.com")
    st.write("📞 **WhatsApp:** [03119883980](https://wa.me/923119883980)")
    
    st.subheader("Follow Our Socials")
    st.markdown(f"""
    <a href="https://www.facebook.com/AliZa1201" target="_blank">Facebook</a> | 
    <a href="https://www.instagram.com/ah_physicist?igsh=cHJ1d3o3eWY2eDJs" target="_blank">Instagram</a>
    """, unsafe_allow_html=True)

with col2:
    st.subheader("Send a Message")
    with st.form("contact"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        msg = st.text_area("How can we help?")
        if st.form_submit_button("Submit"):
            st.success("Message sent! Ali will get back to you soon.")
