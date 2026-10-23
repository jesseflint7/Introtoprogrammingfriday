#week 10 notes functions
#what is a function
# a function is a named set of instructions you can run whenever you want
#functions let us write code once and reuse it when we need it

#def(define) a function: create a function by starting with def
#call a function: run the function by using its name with parantehses
#Paramter: placeholder variable inside the function definition
#argument: The real value that we pass into the function via the parameter

# #create a function that says "Hello"
# def say_hello():
#     print('Hello')
# #call the function
# say_hello()

# #def tells pythons: "Im defining a function"
# #Coder inside the function must be indented
# #nothing runs until you call it

# #parameters and arguments
# def greet(name):
#     #name is a parameter (a placeholder)
#     print("Hello, {name}")
# name=input("Enter your name: ")
# greet(name)
# greet("Carl")
# #Parameters a re like blanks. Arguments fill them in

#the only time we need parameters is when we are passing information from outside the function, into the function
# def greet():
#     name=input("Enter you name")
#     print(f"Hello, {name}")
# greet()

# #print vs return
# #a function that prints:
# def hello_print():
#     print("Hello World")
# #this shows the text to the user 
# #but it does not give a value back to the rest of the program

# #a function that returns :
# def hello_return():
#     return "Return Hello World"
# #This sends a value back to wherever the function was called
# #The caller can store it, print it, etc

# # hello_return()
# # hello_print()
# msg=hello_return()
# print(msg)

# result=hello_print()
# print(result) #this will print none because hello print doesn't return a value back to the function

#print is for the user. return is for the program

# #function example
# #calc program
# def calc(num1,num2):
#     operator=input("What sort of math do you want to do: +,-,*,/")
#     #use if/else to decide what to do
#     #perform the math
#     #print or return the result
#     if operator=="+":
#         return num1+num2
# #function now has the value of 4
# print(calc(1,3)) 

# #fake loop
# #a function can call itself, theis is called recursion
# #a function can behave like aloop if it repeats until a condition is met
# #if a function is calling itself, it must have a stop condition

# #a function that propts user if they want to continue, if user doesn't want to continue "loop" stops
# #if auser says yes, ask them again
# #, if user doesnn't want to continue "loop" stops
# def play_again():
#     answer=input("Again? (y/n): ").lower()
#     if answer=="y":
#         play_again()#calls itself again 
#     else:
#         print("Goodbye")
# play_again()