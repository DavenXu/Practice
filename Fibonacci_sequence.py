### 10項資料前兩項加起來為後一項之答案 ###

numberOfElemnet = 2
ireation = 10
number = []

for i in range(2):
    
    value = int(input(" 請輸入你想輸入的數字 : "))
    number.append(value)

for i in range(2,10):
    value2 = number[ i-1 ] + number[ i-2 ]
    number.append(value2)

print(number)