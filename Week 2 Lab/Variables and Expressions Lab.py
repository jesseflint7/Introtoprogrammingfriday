# CISW 125
# Intro to programming

# Follow the Documentation Policy as it's good practice and will get you used to what you should do for
# your projects and other labs.

# If you're stuck, ask questions. There are no dumb questions.
# ------------------------------------------------------------------------------------------------------
# We're going to play around with variables and expressions today
# The goal is to just test out things and put them to use and possibly
# save the ideas/work for projects down the line.

# Again, the goal is to "play" around and explore. There's no right or wrong to this.
# Just think about input vs output and what we can do with them.
# ------------------------------------------------------------------------------------------------------


# Create some variables, give them a theme. Example: items on a grocery list, games/books/movies you enjoy, etc.
fav_movie="Life of Pi"
fav_movie_snack="popcorn"
fav_drink="root beer"

# Then print your variables.
print(fav_movie)
print(fav_movie_snack)
print(fav_drink)

# Now try to reassign a value. This is essentially "overwriting" your variables data with new data. Python works from top to bottom.
fav_movie="Hot Rod"
fav_movie_snack="sour patch kids"
fav_drink="Dr. Pepper"

# After you've done this, try to print your variables in string using f-strings.
print(f"My favorite movie is {fav_movie} when watching movies I like to eat {fav_movie_snack} and drink {fav_drink}.")

# Next, try to create some expressions that involve addition, subtraction, multiplication, and division
# Store the results of your expressions in a variable and then print the outcome
num1=6
num2=10
num3=25
num4=111
addition=num2+num4
subtraction=num1-num2
division=num3/num1
multiplication=num4*num1
print(addition)
print(subtraction)
print(multiplication)
print(division)

# See if you can find other ways to "do maths" (hint: operators are useful and efficient.)
# https://www.w3schools.com/python/python_operators.asp
print(5+12)
print(5*5)
print(2**6)
print(25-6)
print(50/25)
print(22//3)

# Now, I'd like you to make two variables that contain your first and last name
# After you've made the variables, find a way to join the two strings to print your full name. This is string concatenation.
# Think of it as "adding" your variables together.
first_name="Jesse "
last_name="Flint"
name=first_name+last_name
print(name)

# While we did some math earlier, I'd like you to try doing math with variables this time. (If you already did this, you can skip this. Good job.)


# Lastly, do something of your own choice. Anything that involves variables and expressions is allowed here.
# If you're stumped on ideas, just try and make an expression that converts Celsius to Fahrenheit or vice versa.
games_won=(5+3+9)
print(games_won)


# Upload this to Canvas under the Variable and Expressions Lab assignment.
