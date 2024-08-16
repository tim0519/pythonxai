import streamlit as st
from utils import set_background  # 從utils.py引入set_background函數


set_background("image/bg.png", 60, "left bottom")
st.title("歡迎來到python AI課程")
