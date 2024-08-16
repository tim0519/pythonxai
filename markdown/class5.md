### Markdown筆記 - Python程式技巧

#### 1. 定義函數 (`def`)

- 使用 `def` 關鍵字來定義函數，後面接函數名稱和小括號，最後加上冒號。
- 小括號內可以包含參數，參數用於傳入值。

```python
def hello():
    print("Hello, World!")
```

#### 2. 迴圈與函數結合 (`for` + `def`)

- 使用 `for` 迴圈反覆執行函數。

```python
for i in range(10):
    hello()
```

#### 3. 傳入參數的函數

- 可以在函數中定義參數，並在呼叫函數時傳入資料。

```python
def hello(name):
    print(f"Hello, {name}!")
```

#### 4. 回傳值的函數 (`return`)

- 函數可以回傳一個或多個值，使用 `return` 關鍵字。

```python
def add(a, b):
    return a + b
```

#### 5. 多個回傳值

- 一個函數可以回傳多個值，用逗號分隔。

```python
def add_sub(a, b):
    return a + b, a - b
```

#### 6. 條件式回傳 (`if` + `return`)

- 可以根據條件回傳不同的值。

```python
def add_sub(a, b):
    if a > b:
        return a + b
    else:
        return a - b
```

#### 7. 預設參數

- 可以設定預設參數值，如果呼叫函數時沒有提供該參數，將使用預設值。

```python
def hello(name, message="Hello"):
    print(f"{message}, {name}!")
```

#### 8. 限制傳入參數型態

- 可以在參數中指定型態，並提示使用者應該傳入的型態。

```python
def add(a: int, b: int = 0) -> int:
    return a + b
```

#### 9. 區域變數與全域變數

- 區域變數只能在函數內部使用，函數內部不能直接修改全域變數。

```python
length = 5  # 全域變數

def calculate_square_area():
    area = length**2  # area 是區域變數
    print(area)
```

#### 10. 使用 `global` 修改全域變數

- 使用 `global` 關鍵字來在函數內修改全域變數。

```python
length = 5
area = 100

def calculate_square_area():
    global area
    area = length**2

calculate_square_area()
print("面積是", area)
```

#### 11. 使用 `docstring` 來撰寫函數註解

- 使用 `"""` 來撰寫函數說明，可以包含參數、型態、回傳值等資訊。

```python
def hello(name: str):
    """
    這是一個打招呼的函數。
    參數:
        name: str - 姓名
    回傳值:
        None
    """
    print(f"Hello {name}!")
```

#### 12. 匯入函數 (`import`)

- 可以從其他模組中匯入函數來使用。

```python
from utils import set_background
set_background("image/bg.png", 60, "left bottom")
```

#### 13. 使用 `streamlit` 與 `openai` 模組進行聊天應用

- `streamlit` 用於建立簡單的網頁應用，並使用 `openai` 進行聊天模型交互。

```python
import streamlit as st
import openai
from utils import load_openai_api

openai.api_key = load_openai_api()

if "history" not in st.session_state:
    st.session_state["history"] = []

prompt = st.chat_input("請輸入想要對話的訊息")
if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})
    response = openai.chat.completions.create(
        model=st.session_state.model,
        temperature=0.7,
        messages=[{"role": "system", "content": st.session_state.system_message}]
        + st.session_state.history,
    )
    assistant_message = response.choices[0].message.content
    st.session_state.history.append({"role": "assistant", "content": assistant_message})
    st.rerun()
```
