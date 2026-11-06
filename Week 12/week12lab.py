#Lists

#Creating a list of shopping cart
shopping=["apples","oranges","steak","milk","bread"]
print(len(shopping))#length of shopping items
print(shopping[2])#specific item being printed
shopping.append("eggs")#adding eggs to end of list
shopping.insert(3,"butter")#adding item after 4th item

#List Methods
print(shopping.count("apples"))#counts how many times item is in list
shopping.remove("oranges")#removing an item from the list
shopping.sort()#sorting my list in alphabetical order
shopping.reverse()#reversing my list order


#Dictionaries

#Creating a shopping list with specific amount of each item
shopping_list={
    "apples":10,
    "bananas":6,
    "orages":20,
    "milk":2,
    "butter":1

}
print(shopping_list["apples"])#prints stock level of apples
shopping_list["grapes"]=10#adds grapes to the list
shopping_list["apples"]+=5#adds 5 apples to list
print(shopping_list.keys())#retrieves all keys from dictionary
print(shopping_list.values())#retrieves all values from dictionary

#Iterating over ditionaries
for key in shopping_list.keys():
    print(key)#create and print loop for keys in dictionary
for value in shopping_list.values():
    print(value)#create and print loop for values in dictionary
for key, value in shopping_list.items():
    print(f"{key}:{value}")#create and print key-value items in dictionary


#Nested dictionaries
customers={
    "001":{
        "Name":"John Doe",
        "Items Bought":["apples","oranges"],
        "Total spent":23.50
    },
    "002":{
        "Name":"Jane Doe",
        "Items Bought":["bread","butter"],
        "Total spent":21.20
    }
}
print(customers["001"]["Name"])#accessing specific details


#I have learned how to access the list and dictionaries better now with this class.
#I learned alot through the homework but the class helped me get hands on experience helping me gain a better understanding.
#I thought the nested dictionaries were interesting and I can see alot of uses that you can do with it.
#The things that still confuse me a little is the details sometimes there is small things such as commas or where to place different things to make the code read it better.

#I still am trying to decide what I would like to use this for but i can see by using the dictionaries and list you can access information much easier especially through the nested dictionaries