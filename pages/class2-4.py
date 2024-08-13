import streamlit as st

st.markdown("## 數字金字塔")
number = st.number_input("請輸入一個整數:", step=1, min_value=1, max_value=9)
st.markdown("數字金字塔:")
for i in range(1, number + 1):
    st.markdown(f"{i}" * i)
