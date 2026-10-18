#This program will ask how many things you want to average
#It will then ask for the price of each item and then tell you the average price

count=int(input("How many items do you want to average? "))
total=0
for i in range(count):
    price=float(input("Enter a price: "))
    total+=price
average=total/count
print("The average price is: ", average)
#I recognize that there are some issues here with this program
#If the user hits enter without entering a number it will end the program with an error
#I looked up ways to fix this it can be done by using the try and except functions 
#but didn't understand it well enough yet to try it
#overall this program works as intended though