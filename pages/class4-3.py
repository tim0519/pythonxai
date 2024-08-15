import streamlit as st
import time
import os

image_folder = "image"
image_files = os.listdir(image_folder)

if "products" not in st.session_state:  # 如果session_state中沒有products
    st.session_state.products = {}  # 就建立一個products的session_state

for image_file in image_files:  # 顯示所有圖片
    product_name = image_file[:-4]  # 取得圖片名稱，去掉.png後的部分
    if (
        product_name not in st.session_state.products
    ):  # 如果session_state中沒有product_name
        st.session_state.products[product_name] = {
            "價格": 10,
            "庫存": 10,
            "image": f"{image_folder}/{image_file}",
        }  # 就建立一個product_name的session_state
st.title("購物平台")
col_number = st.number_input("請輸入列數", min_value=1, max_value=10, value=3)
cols = st.columns(col_number)
i = 0
for product_name, details in st.session_state.products.items():
    with cols[i % len(cols)]:  # 取餘數來判斷放在哪一行
        st.image(details["image"], use_column_width=True)
        st.markdown(f"### {product_name}")
        st.markdown(f"價格:{details['價格']}")
        st.markdown(f"庫存:{details['庫存']}")

        if st.button(f"購買 {product_name}", key=f"{product_name}"):
            if details["庫存"] > 0:
                st.session_state.products[product_name]["庫存"] -= 1
                st.success(f"購買{product_name}成功！")
                time.sleep(1)
                st.rerun()
            else:
                st.error(f"{product_name}庫存不足！")
    i += 1

# 新增商品庫存區塊
st.title("新增商品庫存")
product_names = list(st.session_state.products.keys())
# 選擇要補貨的產品
product_name = st.selectbox("請選擇要補貨的產品", product_names)
# 輸入要補貨的數量
quantity = st.number_input("請輸入要補貨的數量", min_value=1, max_value=10, value=1)
