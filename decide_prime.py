### 判斷是不是質數 ###

NUMBER_OF_PRIMES = 50
NUMBER_OF_PRIMES_LINE = 10
count = 0
number = 2 

while count < NUMBER_OF_PRIMES: 

    ISPrime = True

    divisor = 2 
    while divisor <= number / 2 :
        if number % divisor == 0 :
            ISPrime = False
            break
        divisor += 1

    if ISPrime :
        count += 1

        print(format(number,"5d" ), end = '')
        
        if count % NUMBER_OF_PRIMES_LINE == 0 :
            print()

    number += 1