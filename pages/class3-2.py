import streamlit as st

st.title("點餐機")
col1, col2 = st.columns([1, 1])
with col1:
    food = st.text_input("請輸入餐點:")
    if "cargo" not in st.session_state:  # 如果session_state中沒有cargo
        st.session_state.cargo = []  # 就建立一個cargo的session_state
with col2:
    if st.button("加入餐點"):
        st.session_state.cargo.append(food)

st.markdown("購物籃:")
for i in range(len(st.session_state.cargo)):
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write(st.session_state.cargo[i])
    with col2:
        if st.button("刪除", key=i):
            st.session_state.cargo.pop(i)
            st.rerun()
