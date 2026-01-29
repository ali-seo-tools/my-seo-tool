import streamlit as st

st.title("🔗 Professional SEO Services")
st.write("Choose the right growth plan for your business.")

c1, c2 = st.columns(2)
with c1:
    st.markdown("""
    ### 🎖️ Standard Package
    * 5 High-Quality Guest Posts
    * Manual Outreach
    * Do-Follow Links
    * **Price: $49**
    """)
    st.button("Order Standard", key="b1")

with c2:
    st.markdown("""
    ### 🏆 Premium Package
    * 15 High-Quality Guest Posts
    * Content Writing Included
    * Detailed Ranking Report
    * **Price: $149**
    """)
    st.button("Order Premium", key="b2")
