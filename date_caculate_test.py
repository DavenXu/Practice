Today = eval(input(" 請輸入今天星期幾 :"))
numberOfDay = eval(input(" 距離今天天數幾天 :"))

week = ["星期日","星期一","星期二","星期三","星期四","星期五","星期六"]

n = Today + numberOfDay 

if n < len(week) :         # 如果 n 在 week矩陣裡面可以直接算出禮拜幾，幾本上小於七天
    print(week[n])
else:
    i = n % 7              # 對 n 取餘數看還剩下幾天補上去
    print(week[i])
