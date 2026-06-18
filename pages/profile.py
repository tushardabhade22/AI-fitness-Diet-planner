import streamlit as st
import streamlit as st

# LOGIN CHECK
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("🔒 Please login first")
    st.stop()



st.title("👤 Profile")

if "weight" not in st.session_state:
    st.session_state.weight = 70

if "height" not in st.session_state:
    st.session_state.height = 170

if "goal" not in st.session_state:
    st.session_state.goal = "Weight Loss"

name = st.text_input(
    "Name",
    value=st.session_state.get("name", "jack")
)

age = st.number_input(
    "Age",
    min_value=15,
    max_value=80,
    value=st.session_state.get("age", 18)
)

weight = st.number_input(
    "Weight (kg)",
    value=st.session_state.weight
)

height = st.number_input(
    "Height (cm)",
    value=st.session_state.height
)

goal = st.selectbox(
    "Goal",
    ["Weight Loss", "Weight Gain", "Muscle Building"]
)

if st.button("Save Profile"):

    st.session_state.name = name
    st.session_state.age = age
    st.session_state.weight = weight
    st.session_state.height = height
    st.session_state.goal = goal

    st.success("Profile Saved")
    