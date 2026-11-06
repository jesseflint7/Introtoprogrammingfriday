# #How to make a list
# favgames= ["Halo", "Elden Ring", "RE2", "RE2"]

# #Indexing the list
# #searching through a list via its placement
# # print (favgames[0]) #This prints out the first list item
# # print (favgames[1])
# # print (favgames[2])

# #Using the length functioin with a list
# #We can use len() to count how many item are in a list
# # print(len(favgames))

# #adding an item to a list
# #append() adds an item to end of list
# #insert() adds an item to a specific position

# favgames.append("Mario Kart")
# # print(len(favgames))

# #Inserting a list item at a certain position
# favgames.insert(0, "RE4")
# # print(favgames)

# #common list methods
# #count() counts how many times a value appears
# #remove() removes a specific item
# #sort() puts the list in a sorted order
# #reverse() flips the current order of the list

# #count() example
# print(favgames.count("RE2"))

# #remove example
# favgames.remove("RE2")
# print(favgames)

# #sort() example
# favgames.sort()
# print(favgames)

# #reverse() example
# favgames.reverse()
# print(favgames)

# #looping through a list
# #we use a for loop when we want to print out the items in a list

# for game in favgames:
#     print (game)


#dictionaries
#dictionaries are usually accessed by key not position
#we use a dictionary when labels matter and you want to look things up by name

player_stats={"Health":100, "Mana":40, "Level": 7, "Gold": 250}
#"key": Value
#a dicitionary stores data in key-value pairs
#how to access data
print(player_stats["Health"])

#adding and updating dictionary values
#you can add a new key value pair by assigning a new value to a new key
#we can also update a n axisting value or increase it

#adding a new key: value
player_stats["Strength"]=12
print(player_stats)

#update a value

player_stats["Health"]=250
print (player_stats)

#adding a value
player_stats["Gold"]+=50
print(player_stats)

player_stats["Mana"]+=50
print(player_stats)

#keys() and value()
#Keys() shows all dictionary keys
#Values() shows all dictionary values

print(player_stats.keys())
print(player_stats.values())

#looping through dictionaries
#you can loop through keys values or both
# .items() is often the most readable way to show everythging in a dicitionary

#key for loop
for key in player_stats.keys():
    print(key)
#value for loop
for value in player_stats.values():
    print(value)

for key, value in player_stats.items():
    print(f"{key}:{value}")


#nested dicitonaries
students={
    "001":{
        "Name":"Ana",
        "Major":"Cyber",
        "Credits":15,
        "High School info":{
            "GPA":3.5
        }
    },
    "002":{
        "Name":"Sebastian",
        "Major":"Networking",
        "Credits":15
    }
}

#accessing nested dictionary info
#to access nested 
print(students["001"]["High School info"]["GPA"])

#combining a nested dicionary with a list
cars={
    "Honda":{
        "Location":"Japan",
        "Founded":1950,
        "Models":["NSX","Civic","Rebel","Accord"]
    
    }
}
print(cars["Honda"]["Models"])