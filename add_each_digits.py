### 加總整數每一個數 ###

def sumDigit(number):

    if number < 0:
        number = - number

    total = 0

    while number > 0 :

        digit = number % 10                # 把每一位都取餘數
        total = total + digit              # 最後把他加起來
        number = number // 10


    return total


num = eval(input(" 請輸入數字 : "))
ans = sumDigit(num)

print(ans)