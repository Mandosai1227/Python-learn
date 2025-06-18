#import math to use sqrt(n)
import math
x = int(input("please enter how many numbers you want to test\n"))
#verification
def is_prime(n):
    if n <= 1:
        return None
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
# Output
def result_output():
    result = is_prime(n)
    if result == True:
        print(f"{n},your number is prime")
    elif result == False:
        print(f"{n},your number is not prime")
    elif result == None:
        print(f"{n},your number is not prime,not composite number")
#loop
for i in range(x):
    # input a number:
    n = int(input("please enter your number\n"))
    is_prime(n)
    result_output()
print("Thanks use my program to define the number!")






