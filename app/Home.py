import streamlit as st
st.set_page_config(
    page_title="HAQ SAHAYAK",
    layout="wide"
)
st.title("HAQ SAHAYAK")

st.subheader("AI Powered Citizen Service Assistance Platform")

st.write(
    """
    Welcome to HAQ SAHAYAK.
    This platform helps citizens:
    - Apply for Government Services
    - Receive Notifications
    - Access Service Information
    - View Application Analytics
    - Track Applications
    """
)

col1, col2, col3 = st.columns(3)
with col1:
    st.success("Apply for Services")

with col2:
    st.success("Track Applications")

with col3:
    st.success("View Notifications")