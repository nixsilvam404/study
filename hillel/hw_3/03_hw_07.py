import math


def factorial(num):
    facto = 1
    for i in range(1, num + 1):
        facto *= i
    return facto


number = int(input('Enter a number: '))
print(f'The factorial is {factorial(number)}')
print(f'The factorial is {math.factorial(number)}')
