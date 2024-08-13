import streamlit as st

st.markdown("## 數字金字塔")
number = st.number_input("請輸入一個整數:", step=1, min_value=1, max_value=9)
st.markdown("數字金字塔:")
for i in range(1, number + 1):
    st.markdown(f"{i}" * i)

st.markdown("---")
st.markdown("箭頭金字塔")
number = st.number_input("請輸入一個整數:", step=1, min_value=1)
a = ""
for i in range(1, number + 1):
    a = a + (" " * (number - i) + "*" * (2 * i - 1) + "\n")
for i in range(number):
    a = a + (" " * (number - 1) + "*" + "\n")
st.markdown(f"```\n箭頭金字塔:\n{a}\n```")
