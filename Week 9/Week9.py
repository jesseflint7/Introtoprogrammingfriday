#file modes
#when you open a file you give python 2 things
#the filename and the mode

#common modes
# "w" = write
#creates the file if it doesn't exist 
#overwrites the file if it does exist (deletes all the content that was in the file)

#"r" = read only
#you can read the file, but we cannot change it
#error if the file doesn't exist

#"a" = append
#create the file if it doesn't exist
#adds new text to the end without deleting existing content

#with open("folder name/file name, "mode"")
# with open("Week 9/stuff.txt", "r") as file:
#     content=file.read()
#     print(content)

# with open("Week 9/stuff.txt", "w") as file:
#     file.write("This is going to be line 1 \n")
#     file.write("This is going to be on line 2 \n")
#     file.write("This is going to be on line 3")
#     #\n means "new line"
#     #if you forget \n, everything will run together on one line

# with open("Week 9/newfile.txt","w")as file:
#     file.write(New file has been created)


# #reading from a file
# #method a: read the whole file at once
# with open("Week 9/stuff.txt","r") as file:
#     contents=file.read()
#     print(contents)

# #method b: read line by line using a for loop
# with open("Week 9/stuff.txt","r") as file:
#     for line in file:
#         print (line)

# with open("Week 9/stuff.txt","a") as file:
#     file.write("I am adding to this file \n")
#     file.write("Stuff is going to be added to this page")
