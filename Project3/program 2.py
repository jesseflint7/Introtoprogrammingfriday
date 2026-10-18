#This is a program that helps you make a grocery list.
#It will ask you to enter the name of an item.

grocery_list=[]
while True:
    item=input("Enter an item to add to your grocery list (type 'done' when finished): ")
    if item=='done':
        break 
#This is put here to stop the loop when the user is done entering items.
    grocery_list.append(item)
#I added The print grocery list part above print item so that it will put it above the list
print("Your grocery list is: ")
for item in grocery_list:
    print(item)
#We did a grocery list like this as a group activity in class.
#This one is done a little differently but it does the same thing.