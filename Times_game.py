import random

number1 = random.randint(0,10)
number2 = random.randint(0,10)

if number1 < number2 : 
    number1 , number2 = number2 , number1

answer = eval(input("What is " + str(number1) + "x" + str(number2) + " ? :"))

if answer == number1*number2 :
    print(" You are correct. ")
else :
    print(f"Yor are incorrect. The {number1} x {number2} is {number1*number2}")