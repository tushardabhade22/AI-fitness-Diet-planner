import streamlit as st

st.title(" Weight Tracker")
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("🔒 Please login first")
    st.stop()

new_weight = st.number_input(
    "Current Weight",
    min_value=30.0
)

if st.button("Save Weight"):

    if "weight_history" not in st.session_state:
        st.session_state.weight_history = []

    st.session_state.weight_history.append(
        new_weight
    )

st.write(
    st.session_state.get(
        "weight_history",
        []
    )
)
import pandas as pd

if "weight_history" in st.session_state:

    df = pd.DataFrame(
        {
            "Weight":
            st.session_state.weight_history
        }
    )

    st.line_chart(df)