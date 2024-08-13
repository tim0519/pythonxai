### 比較運算子 (Comparison Operators)

- `==`: 判斷兩個值是否相等

  ```python
  print(1 == 1)  # True
  ```

- `!=`: 判斷兩個值是否不相等

  ```python
  print(1 != 1)  # False
  ```

- `<`: 判斷左邊的值是否小於右邊的值

  ```python
  print(1 < 1)  # False
  ```

- `>`: 判斷左邊的值是否大於右邊的值

  ```python
  print(1 > 1)  # False
  ```

- `<=`: 判斷左邊的值是否小於或等於右邊的值

  ```python
  print(1 <= 1)  # True
  ```

- `>=`: 判斷左邊的值是否大於或等於右邊的值

  ```python
  print(1 >= 1)  # True
  ```

### 邏輯運算子 (Logical Operators)

- **`and`**: 在兩個布林值都為真時返回`True`

  ```python
  print(True and True)  # True
  ```

- **`or`**: 在至少一個布林值為真時返回`True`

  ```python
  print(True or False)  # True
  ```

- **`not`**: 返回布林值的相反值

  ```python
  print(not True)  # False
  ```

### 運算子優先順序 (Operator Precedence)

1. `()` 括號：最優先處理
2. `**` 指數運算
3. `//` 整數除法, `%` 取餘數, `/` 除法, `*` 乘法
4. `+` 加法, `-` 減法
5. 比較運算子：`==`, `!=`, `<`, `>`, `<=`, `>=`
6. 邏輯運算子：`and`, `or`, `not`

### 密碼門檢查範例 (Password Door Check Example)

- **`if-elif-else` 條件判斷**：根據密碼判斷輸出不同的訊息

  ```python
  password = input("請輸入密碼:")
  if password == "123456":
      print("歡迎光臨")
  elif password == "2006":
      print("hi Tim")
  elif password == "12345678":
      print("hi hi hi")
  else:
      print("密碼錯誤")
  ```

- **`if-elif-else` 與多個 `if` 的差別**：
  - `elif` 可以排除前面條件已經判斷過的情況，提高效率。
  - 多個 `if` 則會每一個條件都進行判斷，效率較低。

### Streamlit 操作

- **匯入 Streamlit 模組** 並重新命名為 `st`

  ```python
  import streamlit as st
  ```

- **`st.number_input`**：生成一個數字輸入框
  - `step` 參數表示每次輸入的數字增減幅度
  - `min_value` 和 `max_value` 設定輸入數字的範圍

  ```python
  number = st.number_input("請輸入你的分數:", step=0.25, min_value=0.0, max_value=100.0)
  ```

- **`st.markdown`**：顯示文字或 Markdown 格式的內容

  ```python
  st.markdown(f"你輸入的數字是:{number}")
  ```

- **`st.button`**：生成一個按鈕，點擊後可以觸發某些事件

  ```python
  if st.button("balloons"):
      st.balloons()
  ```

- **`st.balloons` 和 `st.snow`**：在網頁上顯示特效（氣球或雪花）

### 迴圈 (Loops)

- **`for` 迴圈**：用於遍歷一個範圍或集合中的元素
  - `range(start, stop, step)`：生成一個範圍序列

  ```python
  for i in range(5):
      print(i)  # 0, 1, 2, 3, 4
  ```

- **使用 `range` 製作數字金字塔**

  ```python
  number = st.number_input("請輸入一個整數:", step=1, min_value=1, max_value=9)
  for i in range(1, number + 1):
      st.markdown(f"{i}" * i)
  ```

### List 操作

- **創建 List**

  ```python
  L = [1, 2, 3, "a", "b", "c"]
  ```

- **取得 List 元素**

  ```python
  print(L[0])  # 1
  ```

- **List 走訪元素**
  - 使用 `for` 搭配 `range` 或直接遍歷 List 元素

  ```python
  for element in L:
      print(element)
  ```

- **List 切片**：取得特定範圍的元素

  ```python
  print(L[::2])  # [1, 3, 'b']
  ```

- **`call by value` 與 `call by reference` 的差異**
  - `call by reference` 會讓變數指向同一個記憶體位置，因此改變其中一個變數的值會影響另一個

  ```python
  a = [1, 2, 3]
  b = a
  b[0] = 2
  print(a, b)  # [2, 2, 3] [2, 2, 3]
  ```

### List 的操作

- **`append`**：在 List 的最後面新增元素

  ```python
  L = [1, 2, 3]
  L.append(4)
  print(L)  # [1, 2, 3, 4]
  ```

- **`remove`**：移除 List 中指定的元素（移除第一個找到的）

  ```python
  L = ["a", "b", "c", "d", "a"]
  L.remove("a")  # 移除第一個 "a"
  ```

- **`pop`**：移除並返回指定 index 的元素

  ```python
  L.pop(0)  # 移除並返回第一個元素
  ```
