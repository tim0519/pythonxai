print([])  # 這是個空的型態
print([1, 2, 3])  # 這是一個有三個元素的list
print([1, 2, 3, "a", "b", "c"])  # 這是一個有六個元素的list
print([1, 2, 3, ["a", "b", "c"]])  # 這是一個有四個元素的list
print([1, True, "a", 1.23])  # 這是一個有四個元素的 list

# list讀取元素
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 1
print(L[1])  # 2
print(L[2])  # 3
print(L[3])  # "a"
print(L[4])  # "b"
print(L[5])  # "c"

# list取長度，也就是list中有幾個元素，不是 index的最大值
L = [1, 2, 3, "a", "b", "c"]
print(len(L))  # 6

# list走訪元素
# 可以透過取得index的方式來找到list中的資料
# 也可以直接把list當作一個範圍來取得資料
# 兩種方式都可以，但看使用的情境是否需要用哪一個方式
L = [1, 2, 3, "a", "b", "c"]
for index in range(len(L)):
    print(L[index])

L = [1, 2, 3, "a", "b", "c"]
for element in L:
    print(element)

print(L[::2])  # [1, 3, b]
print(L[1::2])  # [2, a, c]
print(L[1:4:2])  # [2, a]

# call by value
a = 1
b = a  # 複製a的值給b
b = 2
print(a, b)

# call by reference
a = [1, 2, 3]
b = a  # 把a跟b指向同一個記憶體位置，所以改變b的值，也會改變a的值
b[0] = 2
print(a, b)

a = [1, 2, 3]
b = a.copy()  # 複製a的值給b，但是b跟a指向不同的記憶體位置
b[0] = 2
print(a, b)

# list的append
L = [1, 2, 3]
L.append(4)  # 在L的最後面加上4
print(L)  # [1, 2, 3, 4]

# list的移除元素方式有兩種
# 1. 使用remove，可以移除指定的元素
L = ["a", "b", "c", "d", "a"]
L.remove("a")  # 移除第一個a
# remove代表從頭開始找，一找到就刪除然後結束
# 如果要刪除所有符合項目，要使用迴圈
for i in L:
    if i == "a":
        L.remove(i)
# 2. 使用pop，可以移除指定的index的元素
L = ["a", "b", "c", "d", "a"]
L.pop(0)  # 移除index为0的元素
# 代表pop會移除指定的index的元素
# 如果不指定index，就會移除最後一個元素
L.pop()  # 移除最後一個元素
print(L)
