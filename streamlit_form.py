import streamlit as st
from datetime import datetime

st.title("User Information Form")

form_values = {
    "name": None,
    "height": None,
    "gender": None,
    "date_of_birth": None,
}

min_age_threshold = datetime.now() - 80
max_age_threshold = datetime.now() - 18
min_date = datetime(min_age_threshold, 1, 1)
max_date = datetime(max_age_threshold, 1, 1)

with st.form(key="user_info_form"):
    form_values["name"] = st.text_input("Enter your name: ")
    form_values["height"] = st.number_input("Enter your height (cm): ")
    form_values["gender"] = st.selectbox("Gender", ["Male", "Female"])
    form_values["date_of_birth"] = st.date_input("Enter your birthdate", max_value=max_date, min_value=min_date)

    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        if not all(form_values.values()):
            st.warning("Please fill in all of the fields")
        else:
            st.balloons()
            st.write("### Info")
            for (key, value) in form_values.items():
                st.write(f"{key}: {value}")