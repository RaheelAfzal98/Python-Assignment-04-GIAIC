# ----------------- BMI Checker -----------------

import streamlit as st

# Page title and intro
st.title("Smart BMI Checker")
st.subheader("Quickly find out your Body Mass Index and health category.")

# Two-column layout for inputs
left_col, right_col = st.columns(2)

# Left column for weight
with left_col:
    weight = st.number_input("Weight (in kilograms)", min_value=30.0, max_value=200.0, value=65.0, step=0.1)

# Right column for height
with right_col:
    height = st.number_input("Height (in centimeters)", min_value=120.0, max_value=230.0, value=170.0, step=0.1)

# Calculate BMI when button is clicked
if st.button("Check My BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    bmi_rounded = round(bmi, 2)

    st.write("## Your BMI:", bmi_rounded)

    # Health status message
    if bmi < 18.5:
        st.info("⚠️ Status: Underweight")
    elif 18.5 <= bmi < 25:
        st.success("✅ Status: Normal weight")
    elif 25 <= bmi < 30:
        st.warning("⚠️ Status: Overweight")
    else:
        st.error("🚨 Status: Obese")

    # Display BMI ranges
    with st.expander("📊 BMI Classification Table"):
        st.markdown("""
        | Category        | BMI Range     |
        |-----------------|---------------|
        | Underweight     | Less than 18.5 |
        | Normal Weight   | 18.5 – 24.9    |
        | Overweight      | 25 – 29.9      |
        | Obese           | 30 or more     |
        """)

# Extra info section
with st.expander("ℹ️ Learn more about BMI"):
    st.write("""
    **Body Mass Index (BMI)** is a quick screening tool to estimate if your body weight is healthy.
    
    Keep in mind:
    - BMI doesn’t measure body fat directly.
    - Athletes may have higher BMI due to muscle mass.
    - It's not always accurate for children or older adults.
    """)
