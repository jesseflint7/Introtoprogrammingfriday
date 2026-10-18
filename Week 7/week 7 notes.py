# #What is a loop?
# #Loop repeats code
# #python uses WHILE and FOR loops

# #Repeat this loop 3 times
# for number in range (3):
#     #print hello each time loop runs
#     print('Hello')



# #while loops
# #a while loop repeats while a condition is true
# #create a starting variable 
# number=1
# #keep looping while number is less than or equal to 5
# while number<=5:
#     #print the current value of number
#     print(number)
#     #add 1 to number after each loop
#     number+=1

# #make sure something changes inside a While loop. Other wise you may create an infinite loop

# #While loops with user input
# #a while loop is useful when you want to keep asking until a user gives a valid answer

# #ask user for there age
# age=int(input('Enter your age: '))
# #keep looping is the age is less than 1 or greater than 120
# while age < 1 or age > 120:
#     #tell the user that the input is invalid
#     print('Invalid age')
#     #ask the user to enter their age again
#     age=int(input('Enter your age: '))
# #this runs after loop finishes 
# #loop stops once condition becomes false
# print('Age is valid')

# #FOR loops 
# #a for loop works through items one at a time

# #create a list containing anything
# games=['Mincraft','Mario','Zelda']
# #take one item from the games list one at a time
# for i in games:
#     #print the current game
#     print(i)


# #using RANGE()
# #Range() is a sequence of numbers

# #start at 2 and stop before 8
# for number in range(2,8): 
#     #2 is our starting point and we will stop before 8
#     #print the current number
#     print(number)
#     #remember the ending number in range() is not included

# #loop trhough 2-7
# for number in range(2,8):
#     #multiply number by itself
#     square=number*number
#     print(square)



# #Looping through stings
# #a string can be looped through one character at a time
# #store a string value inside a variable

# word='Tanks'
# #Take one character from the string at a time
# for letter in word:
#     #print the current letter
#     print(letter)

# #using break
# #break stops a loop early
# #loop through numbers one through
# for number in range(1-11):
#     #print current number
#     print(number)
#     #want to stop the loop when number is equal to 5
#     if number==5:
#         #stops the loop immediately
#         break

# #nested loops
# #nested loop is a loop inside another loop
# #outer loop that runs through 1,2,3
# for number in range(1,4):
#     #inner loop also runs through 1,2,3
#     for number2 in range(1,4):
#         #print the current value from both loops 
#         print(number,number2)

# #choosing the right loop
# #use a while loop when repetition depends on a condition
# #keep looping while answer is not yes
# answer=input('Enter yes ')
# while answer !='yes':
#     #ask the user again
#     answer=input('Enter yes ')

#use a for loop when working through items
#go through each item in the list
itemlist=[]
for item in itemlist:
    #print the current item
    print(item)

# #use for with range() when working through numbers
# #loop through number 1-10
# for number in range(1,11):
#     #print the current number
#     print(number)
