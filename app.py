import streamlit as st
from config.settings import APP_TITLE, APP_ICON, LAYOUT
from styles.custom_css import get_custom_css
from components.dietary import display_dietary_plan
from components.fitness import display_fitness_plan
from services.planner import create_agents
from models.user_profile import build_profile
from components.layout import show_header, show_sidebar

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout=LAYOUT,
    initial_sidebar_state="expanded"
)

st.markdown(get_custom_css(), unsafe_allow_html=True)

def main():
    show_header()
    active_tab = show_sidebar()

    if 'dietary_plan' not in st.session_state:
        st.session_state.dietary_plan = {}
        st.session_state.fitness_plan = {}
        st.session_state.qa_pairs = []
        st.session_state.plans_generated = False

    if active_tab == "🧍 Profile & Planner":
        with st.sidebar:
            st.header("🔑 API Configuration")
            gemini_api_key = st.text_input("Gemini API Key", type="password", help="Enter your Gemini API key to access the service")
            
            if not gemini_api_key:
                st.warning("⚠️ Please enter your Gemini API Key to proceed")
                st.markdown("[Get your API key here](https://aistudio.google.com/apikey)")
                return
            
            st.success("API Key accepted!")

        try:
            dietary_agent, fitness_agent = create_agents(gemini_api_key)
        except Exception as e:
            st.error(f"❌ Error initializing Gemini model: {e}")
            return

        st.header("👤 Your Profile")
        col1, col2 = st.columns(2)

        with col1:
            age = st.number_input("Age", min_value=10, max_value=100, step=1)
            height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, step=0.1)
            activity_level = st.selectbox("Activity Level", options=["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extremely Active"])
            dietary_preferences = st.selectbox("Dietary Preferences", options=["Vegetarian", "Keto", "Gluten Free", "Low Carb", "Dairy Free"])

        with col2:
            weight = st.number_input("Weight (kg)", min_value=20.0, max_value=300.0, step=0.1)
            sex = st.selectbox("Sex", options=["Male", "Female", "Other"])
            fitness_goals = st.selectbox("Fitness Goals", options=["Lose Weight", "Gain Muscle", "Endurance", "Stay Fit", "Strength Training"])

        if st.button("🎯 Generate My Personalized Plan", use_container_width=True):
            with st.spinner("Creating your perfect health and fitness routine..."):
                try:
                    user_profile = build_profile(age, weight, height, sex, activity_level, dietary_preferences, fitness_goals)

                    dietary_plan_response = dietary_agent.run(user_profile)
                    fitness_plan_response = fitness_agent.run(user_profile)

                    st.session_state.dietary_plan = {
                        "why_this_plan_works": "High Protein, Healthy Fats, Moderate Carbohydrates, and Caloric Balance",
                        "meal_plan": dietary_plan_response.content,
                        "important_considerations": """
                        - Hydration: Drink plenty of water throughout the day
                        - Electrolytes: Monitor sodium, potassium, and magnesium levels
                        - Fiber: Ensure adequate intake through vegetables and fruits
                        - Listen to your body: Adjust portion sizes as needed
                        """
                    }

                    st.session_state.fitness_plan = {
                        "goals": "Build strength, improve endurance, and maintain overall fitness",
                        "routine": fitness_plan_response.content,
                        "tips": """
                        - Track your progress regularly
                        - Allow proper rest between workouts
                        - Focus on proper form
                        - Stay consistent with your routine
                        """
                    }

                    st.session_state.plans_generated = True
                    st.session_state.qa_pairs = []

                    st.success("✅ Plan successfully generated!")

                except Exception as e:
                    st.error(f"❌ An error occurred: {e}")

    elif active_tab == "🍽️ Diet Plan":
        if st.session_state.plans_generated:
            display_dietary_plan(st.session_state.dietary_plan)
        else:
            st.info("Generate your plan first in the 'Profile & Planner' section.")

    elif active_tab == "🏋️ Fitness Plan":
        if st.session_state.plans_generated:
            display_fitness_plan(st.session_state.fitness_plan)
        else:
            st.info("Generate your plan first in the 'Profile & Planner' section.")

    elif active_tab == "💬 Q&A":
        if st.session_state.plans_generated:
            st.header("❓ Questions about your plan?")
            question_input = st.text_input("What would you like to know?")

            if st.button("Get Answer"):
                if question_input:
                    with st.spinner("Finding the best answer for you..."):
                        try:
                            from google.generativeai import GenerativeModel
                            model = GenerativeModel("gemini-pro")
                            context = (
                                f"Dietary Plan: {st.session_state.dietary_plan.get('meal_plan', '')}\n\n"
                                f"Fitness Plan: {st.session_state.fitness_plan.get('routine', '')}\n"
                                f"User Question: {question_input}"
                            )
                            run_response = model.generate_content(context)
                            answer = run_response.text
                            st.session_state.qa_pairs.append((question_input, answer))
                        except Exception as e:
                            st.error(f"❌ An error occurred while getting the answer: {e}")

            if st.session_state.qa_pairs:
                st.header("💬 Q&A History")
                for question, answer in st.session_state.qa_pairs:
                    st.markdown(f"**Q:** {question}")
                    st.markdown(f"**A:** {answer}")
        else:
            st.info("Generate your plan first to ask questions.")

if __name__ == "__main__":
    main()
