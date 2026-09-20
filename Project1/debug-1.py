# Intro to Programming
# Debug Exercise 2

# This program should add three numbers together.

total = 0
num1 = input("What's the first number? >")
# I decided to use the += symbol to add the numbers to the total 
# I also thought I would use float instead of int just in case someone wanted to use decimal numbers.
total += float(num1)
num2 = input("What's the second number? >")
total += float(num2)
num3 = input("What's the third number? >")
total += float(num3)
print(f"Total is: {total:.2f}")
# I used the .2f I looked up how to do this for project 1 program 2.
# I thought it would be good to use it here to because it gave me a long decimal number the first time I tested the program.

# It took me a minute to figure out the first way 
# I thought this way was a little easier, also I wanted the practice trying another way.
num1 = input("What's the first number? >")
num2 = input("What's the second number? >")
num3 = input("What's the third number? >")
total = float(num1) + float(num2) + float(num3)
print(f"Total is: {total:.2f}")