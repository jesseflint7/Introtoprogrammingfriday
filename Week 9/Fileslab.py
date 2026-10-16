# #Task 1 create a file
# with open("Week 9/newfile.txt","w") as file:
#     file.write("This will be the first line \n")
#     file.write("Hello world \n")
#     file.write("Zelda is the best game \n")

# #Task 2 read from a new file
# with open("Week 9/newfile.txt","r") as file:
#     for line in file:
#         print(line)

# #Task 3 Opening file and adding 2 lines to it
# with open("Week 9/newfile.txt","a") as file:
#     file.write("I will add one line here \n")
#     file.write("I think I will add another line here also \n")

# #Task 4 Is to read the file again
# with open("Week 9/newfile.txt","r") as file:
#     content=file.read()
#     print(content)

# #Task 5 challenge
# birth_year=int(input('What year were you born in? '))
# current_year=int(input('What is the current year? '))
# age=current_year-birth_year
# if age<18:
#     print(f'You are {age} and you are a minor')
# else:
#     print(f'You are {age} and you are an adult')

# with open("Week 9/newfile.txt","a") as file:
#     file.write(f"The year you were born was {birth_year} and {age} years old")