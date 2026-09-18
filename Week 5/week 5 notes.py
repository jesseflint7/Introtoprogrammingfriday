# what is a boolean
# A boolean is a value that is either True or False
# print (5>10)
# print (10<20)
# print (3>74)
# print ("cat" == "Cat")

# #Any expression that evaluates to True or False is a boolean expression
# #if statements use these to decided what to run

# answer=input("Do you want to continue? (yes or no)").lower()
# if answer=="yes":
#     print("Continuing th program....")
# elif answer=="no":
#     print("Exiting the program now")
# else:
#     print("Invalid response")

# grade=int(input(""))

#comparision operators
# == equal to 
# != not equal to
# < less than
# > greater than
# <= less than or equal to
# >= greater than or equal to

# score=85
# print(score>75)
# print(score<75)
# print(score==100)

#using AND & OR
# temp=72
# if temp>72 and temp <=75:
#     print("This is a comfortable room temp")
#     #when using AND both conditions must be true
#     #when using OR one condition must be true

# #I want this program to output ("You dont have class today")
# day="Saturday"
# is_holiday=False
# if day=="Saturday" or day=="Sunday" or is_holiday:
#     print("You dont have class today")
# #This program compares multiple conditions at the same time

# day="Monday"
# is_holiday=False
# if day=="Saturday":
#     print("no class")
# elif day=="Sunday":
#     print("no class")
# elif is_holiday==False:
#     print("Its a holiday")

#chained comparisons
# score=65
# #how to write out 65 is <= score but less than 90
# if 60 <= score < 90: #This is also the exact same as: score>= 60 adn score <90
#     print("Score is passing but not perfect")

#if + elif + else
#this is a simple three catagory example
#this program prints out the shipping cost based on the order price
#when using any sort of money input we will use float
# total=float(input("Enter your order total: "))
# if total<25:
#     print("you get $10")
# elif total<50:
#     print("You get $5 shipping!")
# else:
#     print("Free Shipping")

#compare == & is
# list1=[1,2,3]
# list2=[1,2,3]
# list3=list1
# print(list1==list2) #true (content are equal)
# print(list1 is list2) #false: different objects in memory
# print(list1==list3) # True content is equal
# print(list1 is list3) # True same ID

#== compares value/content
# is compares identity

#two different boxes can have the same stuff inside(==)
#but they're still two different boxes(is)

#multi brand example
#program that tells me if the number is positive or negative

number=int(input("Enter you number"))
if number<0:
    print("Negative")
elif number>0:
    print("Positive")
else:
    print("Your number is 0")