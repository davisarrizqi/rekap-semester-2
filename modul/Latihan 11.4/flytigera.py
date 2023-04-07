import os; os.system('cls' if os.name == 'nt' else 'clear')
import random; import math

def factorial(n):
    if(n == 1): return 1
    return n * factorial(n-1)

def power_recursion(number, power):
    if(power == 1): return number * 1
    return number * power_recursion(number, power-1)

if __name__ == '__main__':
    result = power_recursion(2, 6)
    print(result)