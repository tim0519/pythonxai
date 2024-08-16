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

length = 5
area = 100


def calculate_square_area():
    area = length**2


calculate_square_area()
print("面積是", area)

length = 5
area = 100


def calculate_square_area():
    area = length**2  # area是全域變數,length是全域變數
    return area


area = calculate_square_area()
print("面積是", area)

length = 5
area = 100


def calculate_square_area():
    global area
    area = length**2


calculate_square_area()
print("面積是", area)


def hello(name: str):
    """
    指令說明區\n
    這是一個打招呼的函數\n
    參數:\n
    name: str - 姓名

    回傳None
    """

    print(f"hello {name}!")


from utils import set_background  # 從utils.py引入set_background函數


set_background("image/bg.png", 60, "left bottom")
