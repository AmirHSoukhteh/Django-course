import random

number = random.randint(1,100)

def odd_or_even(number):
    
    if number%2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

odd_or_even(number)