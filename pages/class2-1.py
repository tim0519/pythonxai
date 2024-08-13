# 比較運算子
# print(1 == 1)  # True
# print(1 != 1)  # False
# print(1 < 1)  # False
# print(1 > 1)  # False
# print(1 <= 1)  # True
# print(1 >= 1)  # True

# 邏輯運算子
# and運算子
# print(True and True)  # True
# print(True and False)  # False
# print(False and True)  # False
# print(False and False)  # False

# or運算子
# print(True or True)  # True
# print(True or False)  # True
# print(False or True)  # True
# print(False or False)  # False

# not運算子
# print(not True)  # False
# print(not False)  # True

# 優先順序
# 1. () 括號
# 2. ** 指數
# 3. // 整數除法 % 取餘數 / 除法 * 乘法
# 4. + 加法 - 減法
# 5. == != < > <= >= 比較運算子
# 6. and or not 邏輯運算子

# 密碼門檢查
# password = input("請輸入密碼:")
# if password == "123456":
#     print("歡迎光臨")
# elif password == "2006":
#     print("hi Tim")
# elif password == "12345678":
#     print("hi hi hi")
# else:
#     print("密碼錯誤")
# 連續使用if跟使用 if elif else 的差別
# elif可以排除前面有判斷過的條件，所以縮短判斷的時間
# 但是如果只用多個if，每一個if都被執行，效率會低
