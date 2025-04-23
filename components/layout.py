import streamlit as st
import streamlit as st

def show_header():
    st.markdown("## 🧠 AI Health & Fitness Planner")
    st.markdown("Get your custom diet and fitness plan based on your lifestyle and goals 💪🥗")

def show_sidebar():
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4697/4697253.png", width=100)
    st.sidebar.markdown("### 📂 Navigation")
    return st.sidebar.radio("Choose a section", ["🧍 Profile & Planner", "🍽️ Diet Plan", "🏋️ Fitness Plan", "💬 Q&A"])



def show_header():
    st.markdown("""
    <style>
        .main-title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
        }
        .subtitle {
            font-size: 1.2rem;
            text-align: center;
            color: #777;
        }
        hr {
            border: none;
            height: 2px;
            background: #eee;
            margin: 1rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-title">🧠 AI Health & Fitness Planner</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Get personalized fitness and dietary plans powered by AI 💪🥗</div>', unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)

def show_sidebar():
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/833/833472.png", width=60)
        st.header("Navigation")
        st.markdown("""
        - 💪 **Fitness Plan**
        - 🥗 **Dietary Plan**
        - ❓ **Q&A**
        """)
        st.markdown("---")
        st.caption("Powered by Streamlit & Gemini AI")
