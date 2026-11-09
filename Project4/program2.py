#This program calculates math operations with 2 numbers
#This was part of the program that we worked on in class 
#I just added a few things to make it more user-friendly
def calculate(a, b):
    operator=input("What math operation would you like to do: +,-,*,/ ")
    if operator=="+":
        return float(a)+float(b)
    #I added floats to allow for decimal numbers to be used
    elif operator=="-":
        return float(a)-float(b)
    elif operator=="*":
        return float(a)*float(b)
    elif operator=="/":
        return float(a)/float(b)
    else:
        return "Invalid input"
a=input("Enter your first number ")
b=input("Enter your second number ")
print(calculate(a, b))