# for 迴圈
# for 會搭配in來使用，in的後面會接一個有範圍的東西
# range(5)會產生0,1,2,3,4
# i是迴圈的變數可以自己取名
# 迴圈變數每回合會從範圍裡面取一個資料出來


for i in range(5):
    print(i)
# range(2, 5)的範圍是2,3,4，不包含結尾5
for i in range(2, 5):
    print(i)
# range(5, 0, -1)的範圍是5,4,3,2,1,0
# -1指得是間距，可以是正數或負數
for i in range(5, 0, -1):
    print(i)
