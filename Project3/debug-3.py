# Intro to Programming
# Debug Exercise 3
#
# There are two problems here. One is quite obvious;
# the other is less so. If you need a hint
# send me a message on Canvas or email me ~Tom
# This loop should output numbers from 1 through 10.
while True:
    print("Counting up: ", end=" ")
    for count in range(1, 11): 
#I had to add an 11 here because it stops one number before the number you input.
        print(count, end=" ")
    print("") 
    choice = input("Should I print them again? (y/n)")
    if choice.lower() == 'n':
        break 
# this break stops the loop 