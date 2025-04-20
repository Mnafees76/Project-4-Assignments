import streamlit as st

# Adding custom styles for better appearance 🎨
st.markdown("""
    <style>
        .title {
            color: #4CAF50; 
            font-size: 40px; 
            font-weight: bold;
        }
        .instruction {
            color: #2196F3; 
            font-size: 20px;
        }
        .result {
            font-size: 18px;
            font-weight: bold;
        }
        .underweight {
            color: #FF9800;
        }
        .normal {
            color: #4CAF50;
        }
        .overweight {
            color: #FF5722;
        }
        .obese {
            color: #F44336;
        }
        .error {
            color: #D32F2F;
        }
    </style>
""", unsafe_allow_html=True)

# Setting the title of the app 🏷️ with custom class
st.markdown('<p class="title">BMI Calculator</p>', unsafe_allow_html=True)

# Displaying an instruction message for the user 💡
st.markdown('<p class="instruction">Enter your height and weight to calculate your BMI.</p>', unsafe_allow_html=True)

# Taking height input from the user (in meters) 🌍
height = st.number_input(
    "Height (in meters)", min_value=0.5, max_value=3.0, value=1.75)

# Taking weight input from the user (in kilograms) 🏋️‍♂️
weight = st.number_input(
    "Weight (in kilograms)", min_value=10, max_value=90, value=70)

# Button to calculate BMI when clicked 🔘
if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        # Calculating BMI using the formula: BMI = weight / height^2 📊
        bmi = weight / (height ** 2)
        # Displaying the result to the user 🎯
        st.markdown(f'<p class="result">Your BMI is: {bmi:.2f}</p>', unsafe_allow_html=True)

        # Giving feedback based on the BMI value 📉📈
        if bmi < 18.5:
            st.markdown('<p class="underweight">You are underweight. 🥴</p>', unsafe_allow_html=True)
        elif bmi < 24.9:
            st.markdown('<p class="normal">You have a normal weight. 😃</p>', unsafe_allow_html=True)
        elif bmi < 29.9:
            st.markdown('<p class="overweight">You are overweight. 😕</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="obese">You are obese. ⚠️</p>', unsafe_allow_html=True)

    else:
        # Displaying an error if invalid values are entered ❌
        st.markdown('<p class="error">Please enter valid height and weight values. 🚫</p>', unsafe_allow_html=True)
