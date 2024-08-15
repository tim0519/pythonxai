import streamlit as st
import os

folderPath = "markdown"  # 設定資料夾路徑
files = os.listdir(folderPath)  # 取得資料夾內所有檔案
# 這時候資料夾可能包含其他檔案，我們只需要取得 .md 檔案
files_name = []  # 新增清單用來存放 .md的檔案
for f in files:  # 逐一檢查所有檔案，檢查是否為 .md 檔案
    if f.endswith(".md"):  # 如果是 .md 檔案就加入到清單中
        files_name.append(f)  # 將檔案名稱加入清單

files_name.sort()  # 排序

for f in files_name:  # 逐一檢查清單中的檔案
    # 用with open()讀取檔案內容並存到file變數裡面，模式為r，編碼為utf-8
    # 這樣可以不用擔心檔案讀去後忘記關閉的問題
    with open(f"{folderPath}/{f}", "r", encoding="utf-8") as file:
        # 開啟檔案後可以做很多事情，這裏我們只讀取檔案內容
        content = file.read()
    with st.expander(f[:-3]):  # 使用expander，標題為檔案名稱去掉.md後的部分
        st.markdown(content)  # 將檔案內容輸出到網頁上
