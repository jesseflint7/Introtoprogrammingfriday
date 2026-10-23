#Task 1
def greet_user():
    name=input("Enter you name: ")
    print(f"Your name is {name}")
greet_user()

#Task 2
def calc(num1,num2):
    operator=input("How would you like to calculate this program: +,-,*,/ ")
    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        return num1*num2
    elif operator=="/":
        return num1/num2
    else:
        operator=input("How would you like to calculate this program: +,-,*,/ ")
print(calc(5,4))

#Task 3
def length(fruit):
    return len(fruit)
fruit=input("What is your favorite fruit ")
print(f"Your favorite fruit has {length(fruit)} letters in it.")

#Task 4
def play_again():
    answer=input("Again? (y/n) ").lower()
    if answer=="y":
        play_again()
    elif answer=="n":
        print("goodbye")
play_again()

#Task 5
#This took a little bit of time for me to understand the what exactly the define function was doing but it makes sense now
#I do feel comfortable working with the functions it just takes a minute for me to understand what my program is doing and I have to look at it step by step
