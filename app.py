import streamlit as st

css = f"""
    <style>
    .stAppHeader {{
            background: #0707774f;
            color: white;
        }}

    .stApp {{
        background: linear-gradient(135deg, #5f4b8b, #a785e6);
        color: white;
    }}

    .st-emotion-cache-10c9vv9 {{
        font-size: 44px;
        font-weight: 700;
        color: white;
        text-align: center;
    }}

    .stVerticalBlock {{
        width: 335px;
        margin: auto;
    }}

    .stText {{
        text-align: center;
        font-size: 22px;
        margin-bottom: 20px;
        color: white;
    }}

    [data-testid="stBaseButton-secondary"] {{
        height: 100px;
        width: 100px;
        font-size: 36px;
        font-weight: bold;
        background-color: #a06cd5;
        color: white;
        border-radius: 10px;
        border: 2px solid white;
    }}

    [data-testid="stHeadingWithActionElements"] {{
        text-align: center;
        width: 335px;
    }}

    .st-emotion-cache-1w723zb {{
        padding: 3rem 1rem 10rem;
    }}

    .st-al {{
        color: white;
    }}

    .st-at {{
        background: rgb(255 255 255 / 30%);
        border-radius: 12px;
        padding: 1rem;
        color: white;
        font-size: 20px;
    }}

        .custom-title {{
        font-size: 40px;
        font-weight: 900;
        color: white;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 25px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.6);
        background-color: rgba(255, 255, 255, 0.1);
        padding: 8px;
        border-radius: 12px;
        border: 2px solid #ffffff33;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }}

    .st-bz {{
        background: #0fa13d;
    }}
    </style>
"""

st.markdown(css, unsafe_allow_html=True)

st.markdown("<div class='custom-title'>🎮 Tic Tac Toe Multiplayer</div>", unsafe_allow_html=True)

if 'board' not in st.session_state:
    st.session_state.player = "X"
    st.session_state.board = [""] * 9
    st.session_state.draw = False
    st.session_state.winner = None

def check_win():
    b = st.session_state.board
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
        (0, 4, 8), (2, 4, 6)]
    
    for i, j, k in wins:
        if b[i] == b[j] == b[k] != "":
            return b[i]
        
    if "" not in b:
        st.session_state.draw = True
    return False

def make_move(pos):
    if st.session_state.board[pos] == "" and st.session_state.winner is None:
        st.session_state.board[pos] = st.session_state.player

        winner = check_win()
        if winner:
            st.session_state.winner = winner
        else:
            st.session_state.player = "O" if st.session_state.player == "X" else "X"

cols = st.columns(3)
for r in range(3):
    for c in range(3):
        idx = r * 3 + c
        with cols[c]:
            st.button(
                st.session_state.board[idx] or " ",
                key=idx,
                on_click=make_move,
                args=(idx, ),
                help=f"Click to place {st.session_state.player}"
            )

if st.session_state.winner:
    st.success(f"🎉 Player {st.session_state.winner} wins!")
elif st.session_state.draw:
    st.warning("🤝 It's a draw!")
