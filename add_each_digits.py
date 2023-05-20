### 加總整數每一個數 ### 

def sumDigit(number):

    if number < 0:
        number = - number

    total = 0

    while number > 0 : 
        
        digit = number % 10
        total = total + digit
        number = number // 10


    return total 


num = eval(input(" 請輸入數字 : "))
ans = sumDigit(num)

print(ans)