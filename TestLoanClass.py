### call loan ###
from HW import Loan

def main():
    
    annual = eval(input(" 請輸入幾期 :" ))
    
    numberOfYears = eval(input(" 請輸入幾年 : "))

    loanAmount = eval(input(" 輸入借款數量 :"))

    borrower = input(" 輸入借款人姓名 :")

    loan = Loan(annual, numberOfYears, loanAmount, borrower)

    print(f"借款人的姓名為{loan.getBorrower()},總共要還的金額為{loan.getTotalPayment()}")


main()