import streamlit as st

st.title(" Apply for Service")
st.subheader("Citizen Application Form")
applicant_name = st.text_input("Applicant Name")
process = st.selectbox(
    "Select Service",
    [
        "Birth Certificate",
        "Income Certificate",
        "Old Age Pension"
    ]
)
district = st.selectbox(
    "Select District",
    [
        "Bhubaneswar",
        "Khordha",
        "Cuttack",
        "Puri"
    ]
)
submit = st.button("Submit Application")

if submit:
    st.success("Application Submitted Successfully")