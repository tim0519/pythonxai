import streamlit as st

st.title("欄位元件")
col1, col2, col3 = st.columns(3)  # 分別建立3個欄位
col1.button("按鈕1", key="1")
col2.button("按鈕2", key="2")
col3.button("按鈕3", key="3")

col1, col2, col3 = st.columns([1, 2, 1])  # 分別建立3個欄位
col1.button("按鈕4", key="4")
col2.button("按鈕5", key="5")
col3.button("按鈕6", key="6")

col1, col2, col3 = st.columns([1, 1, 1])  # 分別建立3個欄位
with col1:  # 在欄位1中建立一個按鈕
    if st.button("按鈕7", key="7"):
        st.balloons()
with col2:  # 在欄位2中建立一個按鈕
    if st.button("按鈕8", key="8"):
        st.snow()
with col3:  # 在欄位3中建立一個按鈕
    st.button("按鈕9", key="9")

# 多個columns
cols = st.columns(15)
for i in range(len(cols)):
    with cols[i]:
        if st.button(f"按鈕{i+1}", key=f"{i+10}"):
            st.balloons()

st.markdown("---")
st.title("文字元件")
text = st.text_input("請輸入你的名字和身分證字號:")
if st.button("確認"):
    st.markdown(f"您輸入的是：{text}")
    st.balloons()
if st.button("忘記自己的名字和身分證字號"):
    st.snow()

st.markdown("---")

# columns排列元件效果比較
# 2columns
col1, col2 = st.columns(2)
with col1:
    st.button("按鈕1", key="25")
    st.button("按鈕2", key="26")
    st.button("按鈕3", key="27")
with col2:
    st.write("a")
    st.write("b")
    st.write("c")
# 沒對齊

st.markdown("---")
# 要對齊
for i in range(3):
    col1, col2 = st.columns([1, 1])
    with col1:
        st.button(f"按鈕{i+1}", key=f"{i+28}")
    with col2:
        if i == 0:
            st.write("你好")
        elif i == 1:
            st.write("我好")
        elif i == 2:
            st.write("大家好")

st.markdown("---")
st.title("session_state")
ans = 1
if st.button("按ans然後+1", key="a"):
    ans = ans + 1
st.write(f"ans={ans}")

st.markdown("---")

# session_state
if "ans" not in st.session_state:  # 如果session_state中沒有ans
    st.session_state.ans = 1  # 就建立一個ans的session_state

if st.button("按ans然後+1", key="b"):  # 如果按了ans鍵
    st.session_state.ans = st.session_state.ans + 1  # 就將session_state中的ans加1
st.write(f"ans={st.session_state.ans}")  # 就在畫面上印出session_state中的ans

# 有時候按按鈕不一定會整理頁面，可以用st.rerun()來整理
if st.button("重新整理頁面", key="c"):
    st.rerun()  # 重新整理頁面
