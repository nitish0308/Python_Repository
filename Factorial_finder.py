#Factorial

def factorial_finder(num):
    original_num=num
    factorial_num=1
    while num>0:
        factorial_num= factorial_num*num
        num=num-1
    print(f"factorial of {original_num} is:{factorial_num}")
    return

#factorial_finder(num=5)

import math
n=5
factorial = math.prod([i for i in range(1, n + 1)])

#print(f"The factorial of {n} is {factorial}")


fact = 1
n=3
# The walrus operator updates 'fact' at each step of the loop
[fact := fact * i for i in range(1, n + 1)]

print(f"The factorial of {n} is {fact}")