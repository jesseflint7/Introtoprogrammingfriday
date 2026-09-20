# This program will ask the user for their first and last name then print it.
# It will also tell the user how many characters are in their full name by two seperate lines.
# Lastly it will tell them their initials to their first and last name.
first_name=input('Type in your first name ') 
# I have been experimenting with the single quotes for strings I think I like it a little better 
last_name=input('Now type in your last name ')
print(f'Your name is {first_name} {last_name}')
print(f'Your first name has {len(first_name)} characters.')
print(f'Your last name has {len((last_name))} characters.')
print(f'Your initials are {first_name[0]} and {last_name[0]}') 
# We learned how to index the first character in week 3