num1=7
num2=3.14
# Yes you can do math with both a float and an interger at the same time
print(num1+num2)
num1=input("Enter a whole number " )
num2=input("Enter a decimal value " )

# A string is information within the quotes it holds no numeric value
word="Good morning"
phrase=(f"{word}, Jesse")
print(phrase)
print(phrase[0])
print(phrase[5:10])

# A list can contain any type of data such as numbers or words
mylist=["Resident Evil","Zelda","Metroid",10,22,33]
mylist.append("Call of Duty")
print(mylist)
# It added what I wanted it to the list with the .append()
mylist.remove(10)
print(mylist)
print(len(mylist))

# I have learned that you can really customize your strings. There is many things that python program can do just as long as it is input correctly.
# Some Ideas on how this can be used in projects is for math equations for groups of numbers that are together. 
# Also for user input for someone inputing information and the program responding to them