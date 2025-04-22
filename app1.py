import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open("linear_regression_model.pkl"))

# --- Salary Prediction Section ---
st.title("💰 Salary Prediction App")
st.write("This app predicts the salary based on years of experience using a simple linear regression model.")

years_experience = st.number_input("Enter Years of Experience:", min_value=0.0, max_value=50.0, value=1.0, step=0.5)

if st.button("Predict Salary"):
    experience_input = np.array([[years_experience]])
    prediction = model.predict(experience_input)
    st.success(f"The predicted salary for {years_experience} years of experience is: ₹{prediction[0]:,.2f}")

# --- Divider ---
st.markdown("---")

# --- Quiz Section ---
st.header("🧠 Mini Quiz: Just for Fun")

# Define a question and choices
st.write("What module is used for splitting data in scikit-learn?")

# Dropdown or text input
user_choice = st.selectbox("Choose your answer:", ["sklearn.utils", "sklearn.split", "sklearn.model_selection", "sklearn.preprocessing"])

# Store correct answer in session state
if "correct_word" not in st.session_state:
    st.session_state.correct_word = "sklearn.model_selection"

# Check answer
if st.button("Check Answer"):
    if user_choice == st.session_state.correct_word:
        st.success("🎉 Correct! Well done.")
        st.balloons()  # 🎈 Balloons on correct answer
    else:
        st.error("❌ Oops! Try again.")
