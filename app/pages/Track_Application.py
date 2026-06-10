import streamlit as st

st.title(" Track Application")
application_id = st.number_input(
    "Enter Application ID",
    min_value=1
)
if st.button("Track"):
    st.success(
        f"Tracking Application ID: {application_id}"
    )