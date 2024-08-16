# def 區域變數與全域變數
length = 5  # 全域變數


def calculate_square_area():
    area = length**2  # area是全域變數,length是全域變數
    # 不可以修改全域變數,例如 length = length + ,會出錯
    # 因為在函數內部length是區域變數,不能直接修改全域變數
    print(area)


length = 10
calculate_square_area()
# print("長度是",area) 這行會出錯,因為area是區域變數,只能在函數內部使用
