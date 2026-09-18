#this is a grading system where you enter your score and it will tell you your grade
score=float(input("Enter your score "))
if 100 >= score >= 90:
    print("You have an A")
elif 90 > score >= 80:
    print("You have a B")
elif 80 > score >= 70:
    print("You have a C")
elif 70 > score >= 65:
    print("You have a D")
else:
    print("You have a F")




#this is an age classifier
age=int(input("Enter your age "))
if 0 <= age <= 12:
    print("You are a child")
elif 12 < age <= 19:
    print("You are a teenager")
elif 19 < age <= 64:
    print("You're an adult")
else:
    print("You are a senior")


#this is a password checker
password=input("Enter your password ")  #len is used to count how many characters an object
if len(password)>=8:
    print("Password is the right length")
else:
    print("Password is too short")
    