import os; os.system('cls' if os.name == 'nt' else 'clear')
import random; import math

def factorial(n):
    if(n == 1): return 1
    return n * factorial(n-1)

def power_recursion(number, power):
    if(power == 1): return number * 1
    return number * power_recursion(number, power-1)

def print_fibo(n):
    if(n == 0): return 0
    elif(n == 1): return 1
    return print_fibo(n-1) + print_fibo(n-2)

if __name__ == '__main__':
    result = print_fibo(10)
    print(result)