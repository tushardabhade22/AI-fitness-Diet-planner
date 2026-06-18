import streamlit as st
from PIL import Image

from utils.gemini_helper import analyze_food_image

# LOGIN CHECK
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("🔒 Please login first")
    st.stop()



st.set_page_config(
    page_title="Food Analyzer",
    page_icon="🍔",
    layout="wide"
)

st.title("🍔 Food Analyzer")

st.write("Upload a food image to analyze.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Food Image",
        use_container_width=True
    )

    st.success("Image Uploaded Successfully")

    # Dummy Analysis
st.subheader("📊 Food Analysis")

if st.button("🤖 Analyze Food"):

    with st.spinner("Analyzing food image..."):
        result = analyze_food_image(image)

    st.markdown(result)