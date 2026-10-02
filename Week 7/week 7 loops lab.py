#Part 1
number=1
while number<=5:
    print(number)
    number+=1

#Part 2
day=int(input('Enter what day you were born on '))
while day < 1 or day > 31:
    print('Invalid day')
    day=int(input('Enter what day you were born on '))
print("That's a cool day to be born")

#Part 3
movies=['Life of Pi', 'Hot Rod', 'Big Fish', 'The other guys']
for movie in movies:
    print(movie)

#Part 4
for number in range(2,8):
    print(number)

#Part 5
name=('Jesse Flint')
for letter in name:
    print(letter)

#Part 6
for number in range(1,10):
    print(number)
    if number ==9:
        break

#Part 7
for x in range(10,15):
    for i in range(5,12):
        print(x,i)
#it has to finish printing all of the numbers within the i range before it moves onto the next number in x
#it does this because i is indented within the x variable

