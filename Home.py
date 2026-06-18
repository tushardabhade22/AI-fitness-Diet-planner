import streamlit as st

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="AI Fitness  & Diet Planner",
    page_icon="🏋️",
    layout="wide"
)

# ==================================
# CSS
# ==================================

st.markdown("""
<style>

/* ==========================
   FADE IN ANIMATION
========================== */

.fade-in{
    animation:fadeIn 1s ease-in;
}

@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(20px);
    }

    to{
        opacity:1;
        transform:translateY(0);
    }
}

/* ==========================
   ANIMATED GRADIENT TITLE
========================== */

.gradient-title{
    background:linear-gradient(
        270deg,
        #38bdf8,
        #60a5fa,
        #818cf8,
        #38bdf8
    );

    background-size:400% 400%;

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;

    animation:gradientMove 6s ease infinite;
}

@keyframes gradientMove{
    0%{
        background-position:0% 50%;
    }

    50%{
        background-position:100% 50%;
    }

    100%{
        background-position:0% 50%;
    }
}

/* ==========================
   CARD HOVER EFFECT
========================== */

div[data-testid="metric-container"]{
    background:#1e293b;
    border-radius:15px;
    padding:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.3);
    transition:all 0.3s ease;
}

div[data-testid="metric-container"]:hover{
    transform:translateY(-5px);
    box-shadow:0px 10px 25px rgba(0,0,0,0.4);
}

/* ==========================
   PULSE EFFECT
========================== */

.pulse{
    animation:pulse 2s infinite;
}

@keyframes pulse{
    0%{
        transform:scale(1);
    }

    50%{
        transform:scale(1.02);
    }

    100%{
        transform:scale(1);
    }
}

</style>
""", unsafe_allow_html=True)
# ==========================
# LOGIN SESSION
# ==========================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.markdown("""
    <div class="glass fade-in">
        <h1 class="gradient-title">
            🏋️ AI Fitness & Diet Planner
        </h1>
        <p>Login to continue</p>
    </div>
    """, unsafe_allow_html=True)

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    col1, col2 = st.columns(2)

    with col1:

        login = st.button("Login")

    with col2:

        guest = st.button("Continue as Guest")

    if login:

        if username == "admin" and password == "1234":

            st.session_state.logged_in = True

            st.success("Login Successful")

            st.rerun()

        else:

            st.error("Invalid Credentials")

    if guest:

        st.session_state.logged_in = True

        st.session_state.name = "Guest"

        st.rerun()

    st.stop()
    st.sidebar.button("🚪 Logout")

# ==================================
# SESSION STATE
# ==================================

defaults = {
    "name": "User",
    "age": 18,
    "weight": 70.0,
    "height": 170.0,
    "goal": "Weight Loss",
    "protein_progress": 75,
    "water_progress": 60,
    "workout_progress": 40,
    "workout_streak":0
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ==================================
# BMI
# ==================================

height_m = st.session_state.height / 100

bmi = round(
    st.session_state.weight / (height_m ** 2),
    2
)

# ==================================
# HEADER
# ==================================

st.markdown("""
<div class="glass">
<h1>🏋️ AI Fitness Planner</h1>
<p>Your Personal AI Fitness Coach</p>
</div>
""", unsafe_allow_html=True)

st.subheader(
    f"Welcome {st.session_state.name} 👋"
)

# ==================================
# TOP CARDS
# ==================================

col1, col2, col3, col4,col5 = st.columns(5)

with col1:
    st.metric(
        "BMI",
        bmi
    )

with col2:
    st.metric(
        "Weight",
        f"{st.session_state.weight} kg"
    )

with col3:
    st.metric(
        "Height",
        f"{st.session_state.height} cm"
    )

with col4:
    st.metric(
        "Goal",
        st.session_state.goal
    )
with col5:
    st.metric(
        "🔥 Streak",
        f"{st.session_state.workout_streak} Days"
    )
    

# ==================================
# NUTRITION SECTION
# ==================================

st.divider()

st.subheader("🥗 Nutrition Progress")

st.write("Protein Intake")

st.progress(
    st.session_state.protein_progress
)

st.write(
    f"{st.session_state.protein_progress}%"
)

st.write("Water Intake")

st.progress(
    st.session_state.water_progress
)

st.write(
    f"{st.session_state.water_progress}%"
)

# ==================================
# WORKOUT SECTION
# ==================================

st.divider()

st.subheader("🔥 Workout Progress")

st.progress(
    st.session_state.workout_progress
)

st.write(
    f"{st.session_state.workout_progress}% Completed"
)

# Motivation Message

if st.session_state.workout_streak >= 7:
    st.success("🏆 Amazing! 7+ day workout streak")

elif st.session_state.workout_streak >= 3:
    st.info("🔥 Great consistency! Keep going")

else:
    st.warning("💪 Start today's workout and build your streak")

# QUICK ACTIONS

st.divider()

st.subheader("⚡ Quick Actions")

col1, col2 = st.columns(2)

with col1:
    st.button("🏋️ Generate Workout")

with col2:
    st.button("🍎 Generate Diet")
if st.button("🔥 Complete Today's Workout"):
    st.session_state.workout_streak += 1
    st.success("Workout completed!")

# ==================================
# FOOTER
# ==================================

st.divider()

st.success(
    "Dashboard Loaded Successfully"
)
# Logout Button
if st.sidebar.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.rerun()