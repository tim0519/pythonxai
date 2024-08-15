# 字典
# dict是透過key-value對組成的，key是唯一的，value可以重複
# dict是無序的，所以無法透過index來取得資料
# dict的key必須是不可變的資料型態 ， 例如:int ,float, string
# dict的value可以是任意資料型態
# dict的key-value是透過冒號來連接， key:value
# dict的key-value是透過逗號來分隔
d = {"a": 1, "b": 2, "c": 3}

# 取得dict的key
print(d.keys())  # ['a', 'b', 'c']
for key in d.keys():  # 逐一取得key
    print(key)  # a b c

# 取得dict的value
print(d.values())  # [1, 2, 3]
for value in d.values():  # 逐一取得value
    print(value)  # 1 2 3

# 取得dict的key-value
print(d.items())  # [('a', 1), ('b', 2), ('c', 3)]
for key, value in d.items():  # 逐一取得key-value
    print(key, value)  # a 1 b 2 c 3

# 新增/修改dict的key-value
d["d"] = 4  # 新增
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d["a"] = 5  # 修改
print(d)  # {'a': 5, 'b': 2, 'c': 3, 'd': 4}

# 檢查dict是否包含某個key
# in不能檢查value
# 跟list比較，in可以檢查的是list的元素與dict的key
print("a" in d)  # True
print("d" in d)  # True
print("e" in d)  # False
print("b" in d)  # true

# 刪除dict的key-value , pop()方法
# 如果資料有存在，就刪除並回傳value
print(d.pop("a"))
# 如果資料不存在，就回傳預設值
print(d.pop("e", "Not Found"))
# 如果資料不存在也沒有預設值，就會报錯

# 比較複雜的dict
d = {"a": [1, 2, 3], "b": {"c": 4, "d": 5}}
print(d["a"])  # [1, 2, 3]
print(d["a"][0])  # 1
print(d["b"])  # {'c': 4, 'd': 5}
print(d["b"]["c"])  # 4

# 成績登記系統，key是學生名字，value是學生的成績，每個科目有3個成績
grade = {
    "陳冠廷1": {"國文": [90, 80, 70], "數學": [80, 90, 60], "物理": [70, 80, 90]},
    "陳冠廷2": {"國文": [80, 90, 70], "數學": [90, 80, 60], "物理": [70, 90, 80]},
    "陳冠廷3": {"國文": [90, 80, 70], "數學": [80, 90, 60], "物理": [70, 80, 90]},
}

# 取得成績
print(grade["陳冠廷1"]["國文"])  # [90, 80, 70]
print(grade["陳冠廷2"]["數學"][2])  # 60
print(grade["陳冠廷3"]["物理"][1])  # 80

# 印出每一位同學的國文段考平均成績
for name, subjects in grade.items():
    # 取得國文成績
    chinese = subjects["國文"]
    # 計算平均成績
    avg = sum(chinese) / len(chinese)
    print(f"{name} 的國文段考平均成績為 {avg:.2f}")  # 到小數點兩位

for name, subjects in grade.items():
    # subject指的是{"國文": [90, 80, 70], "數學": [80, 90, 60], "物理": [70, 80, 90]}
    total = 0
    for scores in subjects.values():
        # subjects.values()是取得{"國文": [90, 80, 70], "數學": [80, 90, 60], "物理": [70, 80, 90]}的value
        total += sum(scores)
    avg = total / (len(subjects) * 3)
    print(f"{name} 的總平均成績為 {avg:.2f}")

# 要某科目的所有成績
avg_grade = {"國文": [], "數學": [], "物理": []}
# 逐一取得每一位同學成績
for subjects in grade.values():  # 取得每一位同學的各科成績
    # subjects = {"國文": [90, 80, 70], "數學": [80, 90, 60], "物理": [70, 80, 90]}
    # 逐一取出每一位同學的各科成績
    for subject, scores in subjects.items():  # 取得每一位同學的某一科目的成績
        # scores = [90, 80, 70]
        # 將各科成績加入avg_grade
        avg_grade[subject] += scores
print(avg_grade)

# dict取長度，取得dict的key的數量
print(len(avg_grade))  # 3
