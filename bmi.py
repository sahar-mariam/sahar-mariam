import streamlit as st

def calculate_bmi(weight, height):
   #Calculate BMI based on weight (in kg) and height (in cm)
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    #interpreting BMI value
    if bmi < 18.5:
        return "You are underweight. Consider gaining weight in a healthy way."
    elif bmi >= 18.5 and bmi < 25:
        return "You are within the normal weight range."
    elif bmi >= 25 and bmi < 30:
        return "You are overweight. Consider losing weight in a healthy way."
    elif bmi >= 30:
        return "You are obese. Consider consulting a healthcare provider."

# streamlit interface
st.title('Simple BMI Calculator')

weight = st.number_input('Enter your weight (in kg)')
height = st.number_input('Enter your height (in cm)')

if st.button('Calculate BMI'):
    bmi = calculate_bmi(weight, height)
    st.write(f'Your BMI: {bmi:.2f}')
    
    bmi_info = interpret_bmi(bmi)
    st.write(bmi_info)
