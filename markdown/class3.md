以下是使用到的程式技巧的筆記，已經轉換成 Markdown 格式：

```markdown
# Streamlit 使用技巧

## 1. 建立欄位
```python
import streamlit as st

st.title("欄位元件")
col1, col2, col3 = st.columns(3)  # 分別建立3個欄位
col1.button("按鈕1", key="1")
col2.button("按鈕2", key="2")
col3.button("按鈕3", key="3")
```

## 2. 設定欄位比例

```python
col1, col2, col3 = st.columns([1, 2, 1])  # 設定欄位比例
col1.button("按鈕4", key="4")
col2.button("按鈕5", key="5")
col3.button("按鈕6", key="6")
```

## 3. 使用 `with` 建立欄位內元件

```python
col1, col2, col3 = st.columns([1, 1, 1])  # 設定欄位比例
with col1:
    if st.button("按鈕7", key="7"):
        st.balloons()
with col2:
    if st.button("按鈕8", key="8"):
        st.snow()
with col3:
    st.button("按鈕9", key="9")
```

## 4. 使用多個欄位

```python
cols = st.columns(15)
for i in range(len(cols)):
    with cols[i]:
        if st.button(f"按鈕{i+1}", key=f"{i+10}"):
            st.balloons()
```

## 5. 文字元件與按鈕

```python
st.title("文字元件")
text = st.text_input("請輸入你的名字和身分證字號:")
if st.button("確認"):
    st.markdown(f"您輸入的是：{text}")
    st.balloons()
if st.button("忘記自己的名字和身分證字號"):
    st.snow()
```

## 6. 欄位排列效果比較

```python
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
```

## 7. `session_state` 使用

```python
st.title("session_state")
ans = 1
if st.button("按ans然後+1", key="a"):
    ans = ans + 1
st.write(f"ans={ans}")

# session_state 使用
if "ans" not in st.session_state:
    st.session_state.ans = 1

if st.button("按ans然後+1", key="b"):
    st.session_state.ans += 1
st.write(f"ans={st.session_state.ans}")

# 重新整理頁面
if st.button("重新整理頁面", key="c"):
    st.rerun()
```

## 8. 點餐機應用

```python
st.title("點餐機")
col1, col2 = st.columns([1, 1])
with col1:
    food = st.text_input("請輸入餐點:")
    if "cargo" not in st.session_state:
        st.session_state.cargo = []
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
```

# Python 基本語法與運算

## 1. 算術指定運算子

```python
a = 1
a += 1  # a = a + 1
print(a)
a -= 1  # a = a - 1
print(a)
a *= 2  # a = a * 2
print(a)
a /= 2  # a = a / 2
print(a)
a //= 2  # a = a // 2
print(a)
a %= 2  # a = a % 2
print(a)
a **= 2  # a = a ** 2
print(a)
```

## 2. 優先順序

```markdown
1. () 括號
2. ** 指數
3. // 整數除法 % 取餘數 / 除法 * 乘法
4. + 加法 - 減法
5. == != < > <= >= 比較運算子
6. and or not 邏輯運算子
7. = += -= *= /= //= %= **=
```

## 3. 迴圈

### while 迴圈

```python
i = 0
while i < 10:
    print(i)
    i += 1  # i = i + 1
```

### break 跳出迴圈

```python
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1  # i = i + 1
```

### for 迴圈

```python
for i in range(10):
    print(i)
    if i == 5:
        break
```

## 4. 隨機數

```python
import random

print(random.randrange(7))
print(random.randrange(1, 6))
print(random.randrange(1, 6, 2))

print(random.randint(1, 6))
```

## 5. 猜數字遊戲

```python
import random

number_to_guess = random.randint(1, 100)
min_user_guess = 1
max_user_guess = 100

while True:
    user_guess = int(input(f"請輸入{min_user_guess}到{max_user_guess}之間的數字: "))

    if user_guess < number_to_guess:
        print("太低了！")
        if user_guess > min_user_guess:
            min_user_guess = user_guess
    elif user_guess > number_to_guess:
        print("太高了！")
        if user_guess < max_user_guess:
            max_user_guess = user_guess
    else:
        print("恭喜你！你猜對了！")
        break
```

```

這些筆記涵蓋了你所提供程式碼中使用的主要技巧，包括 Streamlit 的欄位元件、`session_state` 的使用、基本 Python 運算符、迴圈和隨機數的使用等。
