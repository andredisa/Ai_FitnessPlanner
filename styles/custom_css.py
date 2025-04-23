def get_custom_css():
    return """
        <style>
        .main {
            padding: 2rem;
        }
        .stButton>button {
            width: 100%;
            border-radius: 5px;
            height: 3em;
        }
        .success-box {
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #f0fff4;
            border: 1px solid #9ae6b4;
        }
        .warning-box {
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #fffaf0;
            border: 1px solid #fbd38d;
        }
        div[data-testid="stExpander"] div[role="button"] p {
            font-size: 1.1rem;
            font-weight: 600;
        }
        </style>
    """
