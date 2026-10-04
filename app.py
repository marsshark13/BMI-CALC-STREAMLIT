import streamlit as st

st.set_page_config(
    page_title="BMI Calculator",

    layout="centered"
)


st.write("Calculate your Body Mass Index easily.")

st.divider()

st.header("Personal Information")

name = st.text_input("Enter your name:")

col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Enter your weight in kg:")

with col2:
    height = st.number_input("Enter your height in meters:")

st.divider()

if st.button("Calculate BMI", use_container_width=True):

    try:
        if name.strip() == "":
            raise ValueError("Name cannot be empty.")

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be greater than 0.")

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        st.success(f"{name}, your BMI is {bmi:.2f}")
        st.info(f"Category: {category}")

    except ValueError as e:
        st.error(e)