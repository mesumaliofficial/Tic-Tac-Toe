import streamlit as st

st.title("Tic Tac Toe")

if 'board' not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.player = "X"
    st.session_state.winner = None
    st.session_state.draw = False

def check_win():
    b = st.session_state.board
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for i, j, k in wins:
        if b[i] == b[j] == b[k] and b[i] != "":
            return b[i]
    if "" not in b:
        st.session_state.draw = True
    return None
    
def make_move(pos):
    if st.session_state.board[pos] == "" and st.session_state.winner is None:
        st.session_state.board[pos] = st.session_state.player
        winner = check_win()
        if winner:
            st.session_state.winner = winner
        else:
            st.session_state.player = "O" if st.session_state.player == "X" else "X"

# Layout
cols = st.columns(3)
for i in range(3):
    for j in range(3):
        idx = i * 3 + j
        with cols[j]:
            st.button(
                st.session_state.board[idx] or " ",
                key=idx, on_click=make_move, args=(idx, ),
                help=f"Click to place {st.session_state.player}")


if st.session_state.winner:
    st.success(f"🎉 Player {st.session_state.winner} wins!")
elif st.session_state.draw:
    st.warning("🤝 It's a draw!")


