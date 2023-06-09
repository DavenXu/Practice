## 練習程式寫出一個某一年某一月的日期 ##

def printMonth( year , month) :
    printMonthTitle(year , month)
    printMonthBody(year , month)

def printMonthTitle(year , month ) :
    print("         ",getMonthName(month)," " , year)
    print("------------------------------------------")
    print("  SUN  MON  TUE  WED  THU  FRI  SAT  ")

def printMonthBody(year , month ):
    
    startDay =getStartDay(year , month)

    numOfDaysInMonth = getNumberOfDaysInMonth(year, month)
    i = 0
    for i in range(0 , startDay) : 
        print("    ",end = " ")
    
    for i in range(1 , numOfDaysInMonth + 1) :
        print(format(i , "4d"), end = " ")
        
        if ( i + startDay) % 7 == 0 :
            print()

def getMonthName(month) :
    
    if month == 1 :
        monthName = " January "
    elif month == 2 : 
        monthName = " February "
    elif month == 3 : 
        monthName = " March "
    elif month == 4 : 
        monthName = " April "
    elif month == 5 : 
        monthName = " May "
    elif month == 6 : 
        monthName = " June "
    elif month == 7 : 
        monthName = " July "
    elif month == 8 : 
        monthName = " August "
    elif month == 9 : 
        monthName = " September "
    elif month == 10 : 
        monthName = " October "
    elif month == 11 : 
        monthName = " November "            
    elif month == 12 : 
        monthName = " December "
    else:
        monthName = " 沒有這個日期 87 "
    return monthName

def getStartDay(year , month ):
    START_DAY_1800 = 3

    totalNumberDays = getTotalNumberOfDays(year , month)

    return (totalNumberDays + START_DAY_1800 ) % 7 

def getTotalNumberOfDays(year , month ):
    total = 0

    for i in  range(1800 , year ) :
        if isLeapYear( i ) :
            total = total + 366
        else : 
            total = total + 365

    for i in range(1 , month) :
        total = total + getNumberOfDaysInMonth(year , i)

    return total 

def getNumberOfDaysInMonth(year , month) : 
    if (month == 1 or month ==3 or month ==5 or month == 7 or month == 8 
        or month == 10 or month == 12 ):
        return 31 
    
    if (month == 4 or month == 6 or month == 9 or month == 11) :
        return 30 
    
    if  month == 2 :
        return 29 if isLeapYear(year) else 28
    
    return 0 

def isLeapYear(year) :
   return year % 400 == 0 or ( year % 4  == 0 and year % 100 != 0)

def main() : 
    year = eval(input(" 輸入你想搜尋的年份 : "))
    month = eval(input(" 輸入你想搜尋的月份 : "))

    printMonth(year , month)

main()

