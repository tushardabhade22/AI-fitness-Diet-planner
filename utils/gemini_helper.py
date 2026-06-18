from google import genai
import streamlit as st

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

def ask_gemini(prompt):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
def analyze_food_image(image):

    prompt = """
    Analyze this food image and provide:

    🍔 Food Name
    🔥 Estimated Calories
    💪 Protein (grams)
    🍚 Carbohydrates (grams)
    🥑 Fat (grams)
    ⭐ Health Rating out of 10

    Keep the response concise and well formatted.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[image, prompt]
        )

        return response.text

    except Exception:
        return "❌ Gemini is busy right now. Please try again later."