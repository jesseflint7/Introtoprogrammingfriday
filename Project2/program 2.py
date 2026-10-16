#This program will calculate your age based on the year you were born and the current year.
#It will also use if statements to tell you if you are a minor or an adult.

birth_year=int(input('What year were you born in? '))
current_year=int(input('What is the current year? '))
age=current_year-birth_year
if age<18:
    print(f'You are {age} and you are a minor')
else:
    print(f'You are {age} and you are an adult')

#We did an age classifier in week 5 lab.
#This one is a little different because it tells you your age based on the year your born and the current year.