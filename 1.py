import streamlit as st

# Define background and text colors
BG_COLOR = "linear-gradient(135deg, #8052ec, #d161ff)"
TEXT_COLOR = "#ffffff"

# Define custom CSS to apply styles to the app
css = f"""
    <style>
        .stApp {{
            background: {BG_COLOR};
            color: {TEXT_COLOR};
        }}
        .stAppHeader {{
            background: {BG_COLOR};
            color: {TEXT_COLOR};
        }}
        [data-testid="stBaseButton-secondary"] {{
            height: 100px;
            width: 100px;
            color: purple;
        }}
        .st-emotion-cache-10c9vv9 {{
            font-size: 44px;
        }}
        .stVerticalBlock {{
            width: 335px;
            margin: auto;
        }}
        .stText {{
            text-align: center;
            font-size: 22px;
            margin-bottom: 20px;
        }}
        [data-testid="stHeadingWithActionElements"] {{
        text-align: center;
        width: 665px;
        }}

        .st-emotion-cache-1w723zb {{
        padding: 3rem 1rem 10rem;
        }}
        .st-al {{
        color: white;
        }}

        .st-at {{
        background: rgb(33 195 84 / 67%);
        }}


    </style>
"""
st.markdown(css, unsafe_allow_html=True)


st.title("🎮 Tic-Tac-Toe")

# Game board layout
col1, col2, col3 = st.columns(3)

with col1:
    st.button("0")
    st.button("1")
    st.button("2")

with col2:
    st.button("3")
    st.button("4")
    st.button("5")

with col3:
    st.button("6")
    st.button("7")
    st.button("8")

st.success("you are win")