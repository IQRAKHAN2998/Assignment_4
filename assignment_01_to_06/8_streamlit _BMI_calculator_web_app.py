
import streamlit as st

def calculate_bmi(weight, height):
    """Formula for BMI calculation: weight in kg divided by height squared in meters."""
    return round(weight / (height ** 2), 2)

def main():
    st.title("🔍 BMI Calculator")
    st.write("Check your BMI and understand your health better!")

    # User Input
    weight = st.number_input("Weight (kg):", min_value=1.0, format="%.2f")
    height = st.number_input("Height (m):", min_value=0.5, format="%.2f")

    if st.button("Find My BMI"):
        if height > 0:
            bmi = calculate_bmi(weight, height)
            st.success(f"🎯 Your BMI is: {bmi}")

            # BMI Health Range
            if bmi < 18.5:
                st.warning("🥗 Underweight - Consider eating more nutritious meals!")
            elif 18.5 <= bmi < 24.9:
                st.success("🎉 Normal weight! Keep up the good work!")
            elif 25 <= bmi < 29.9:
                st.warning("⚠️ Overweight - A healthy lifestyle is key!")
            else:
                st.error("🚨 Obesity - Consider making lifestyle adjustments.")
        else:
            st.error("❌ Invalid height input.")

if __name__ == "__main__":
    main()
