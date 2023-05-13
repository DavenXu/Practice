dollar = eval(input(" 請輸入您的本金 :"))
rate = eval(input(" 請輸入年利率是多少 : ")) / 1200 
month = eval(input(" 請輸入您的月數 : "))

dollars = [dollar]

for i in range(month-1):
    total = (dollars[i] + dollar) * (1 + rate)
    dollars.append(total)

print(f"{month}個月可以獲得的金額是 : {dollars[-1]}")