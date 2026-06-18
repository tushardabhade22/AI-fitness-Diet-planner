import streamlit as st
from utils.gemini_helper import ask_gemini


# LOGIN CHECK
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("🔒 Please login first")
    st.stop()

st.title("workout")

st.title("🏋️ Workout Planner")


if "workout_progress" not in st.session_state:
    st.session_state.workout_progress = 0

if "workout_streak" not in st.session_state:
    st.session_state.workout_streak = 0
workout_type = st.selectbox(
    "Workout Type",
    [
        "Home Workout",
        "Gym Workout"
    ]
)

level = st.selectbox(
    "Experience Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

days = st.slider(
    "Workout Days Per Week",
    3,
    7,
    5
)

if st.button("Generate Workout Plan"):

    prompt = f"""
    Create a {days}-day workout plan.

    Workout Type: {workout_type}
    Experience Level: {level}

    Give:
    - Day-wise schedule
    - Exercises
    - Sets and reps
    - Warm-up
    - Rest periods
    - Cool-down

    Format nicely with headings.
    """

    with st.spinner("🤖 Generating AI Workout Plan..."):
        workout_plan = ask_gemini(prompt)

    st.session_state.workout_plan = workout_plan

if "workout_plan" in st.session_state:

    st.subheader("Generated Plan")

    st.text(
        st.session_state.workout_plan
    )

# Progress Tracking

st.divider()

st.subheader("Workout Completion")

completed = st.slider(
    "Completed Percentage",
    0,
    100,
    st.session_state.workout_progress
)

if st.button("Save Progress"):

    st.session_state.workout_progress = completed

    st.success(
        "Progress Updated"
    )
if st.button("🔥 Complete Today's Workout"):

    st.session_state.workout_streak += 1

    st.success(
        f"Workout Completed! Current Streak: {st.session_state.workout_streak} days"
    )

st.divider()
