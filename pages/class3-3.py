# 算術指定運算子
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


# 優先順序
# 1. () 括號
# 2. ** 指數
# 3. // 整數除法 % 取餘數 / 除法 * 乘法
# 4. + 加法 - 減法
# 5. == != < > <= >= 比較運算子
# 6. and or not 邏輯運算子
# 7. = += -= *= /= //= %= **=

# while迴圈
# while會搭配一個條件式來使用
# 條件式為True時會一直執行迴圈
# 條件式為False時會跳出迴圈
# 每次迴圈執行完都會重新檢查條件有沒有變成False
i = 0
while i < 10:
    print(i)
    i += 1  # i = i + 1

# break跳出迴圈
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1  # i = i + 1

for i in range(10):
    print(i)
    if i == 5:
        break

import random  # 匯入random模組

# random.randrange()設定抽籤範圍和range一樣
print(random.randrange(7))
print(random.randrange(1, 6))
print(random.randrange(1, 6, 2))

# random.randint()設定抽籤範圍的方式一定要設定開始與結束
print(random.randit(1, 6))
