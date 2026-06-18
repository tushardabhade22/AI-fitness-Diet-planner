import streamlit as st
from utils.gemini_helper import ask_gemini

st.title("🍎 Diet Planner")

# LOGIN CHECK
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("🔒 Please login first")
    st.stop()

# Diet Type
diet = st.selectbox(
    "Diet Type",
    [
        "Vegetarian",
        "Non-Vegetarian",
        "Vegan"
    ]
)

# Country
country = st.text_input(
    "Country",
    value="India"
)

# Budget
budget = st.selectbox(
    "Daily Budget",
    [
        "Under ₹100",
        "₹100 - ₹200",
        "₹200 - ₹300",
        "Above ₹300"
    ]
)

# Generate Diet
if st.button("🍎 Generate Diet"):

    prompt = f"""
Create a healthy and budget-friendly diet plan.

Country: {country}
Goal: {st.session_state.goal}
Weight: {st.session_state.weight} kg
Diet Type: {diet}
Daily Budget: {budget}

Requirements:
- Use affordable, locally available foods
- Include Breakfast, Lunch, Dinner and Snacks
- Mention approximate calories
- Mention protein target
- Mention water intake
- Suggest inexpensive alternatives if possible

Format the response with headings and emojis.
"""

    with st.spinner("🤖 Generating Diet Plan..."):
        diet_plan = ask_gemini(prompt)

    st.session_state.diet_plan = diet_plan

# Display Plan
if "diet_plan" in st.session_state:
    st.markdown(st.session_state.diet_plan)