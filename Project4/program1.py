#I am going to add two new lines to a file
#Then the program will read a file and print what is says
with open("Project4/program1file.txt","w") as file:
    file.write("This is the first line of this file text\n")
    file.write("I doesn't have any useful information here\n")
    file.write("Here are some useless facts\n")
    file.write("Rubberbands last longer when refrigerated\n")
    file.write("Bees can fly higher than Mount Everest\n")
# I had to create the file first before I could add new lines to it.
with open("Project4/program1file.txt","a") as file:
    file.write("Edgar Allan Poe married his 13 year old cousin\n")
    file.write("It snows metal on venus")
with open("Project4/program1file.txt","r") as file:
    content = file.read()
    print(content) 
    #I like to print it like this a little better than the second way that I have commented out below
    # for line in file:
    #     print(line)