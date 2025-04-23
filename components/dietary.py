import streamlit as st

def display_dietary_plan(plan_content):
    with st.expander("📋 Your Personalized Dietary Plan", expanded=True):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("### 🎯 Why this plan works")
            st.info(plan_content.get("why_this_plan_works", "Information not available"))
            st.markdown("### 🍽️ Meal Plan")
            st.write(plan_content.get("meal_plan", "Plan not available"))
        with col2:
            st.markdown("### ⚠️ Important Considerations")
            for c in plan_content.get("important_considerations", "").split('\n'):
                if c.strip(): st.warning(c)
