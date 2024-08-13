import streamlit as st  # 匯入streamlit模組並重新命名為st

number = st.number_input("請輸入你的分數:", step=0.25)
# step參數表示每次輸入的數字的十進制最小值
st.markdown(f"你輸入的數字是:{number}")
# st.markdown 是在網站上顯示文字用的

st.markdown("---")

import streamlit as st

number = st.number_input("請輸入你的分數:", step=0.25, min_value=0.0, max_value=100.0)

if number >= 90:
    st.markdown("A")
elif number >= 80:
    st.markdown("B")
elif number >= 70:
    st.markdown("C")
elif number >= 60:
    st.markdown("D")
else:
    st.markdown("F")

st.markdown("---")
st.markdown("### 按鈕練習")
# st.button 可以在網站上顯示按鈕
# key參數用來定義按鈕的名稱
if st.button("balloons", key="balloons"):
    st.balloons()
if st.button("snow", key="snow"):
    st.snow()

st.markdown("---")
