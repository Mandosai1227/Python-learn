import math
import numpy

#define run times
x = int(input("you want num of execute"))
#loop
for i in range(x):
    try:
        # input digit number
        user_number = input("please input one digit number like 1e130")
        number = float(user_number)
        print("your number is :", number)
        # change float into int
        number1 = int(number)
        # calculate the num of digit
        out_number = int(math.log10(number1) + 1)
        # output
        print("your number of digit is :", out_number)
    except ValueError:
        print("your number is not for format")
#thanks
print("thanks to use our program")
