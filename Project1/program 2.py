# This program will ask the user for the bill and how many people are in the party. 
# After that it will split the bill and let them know how much they each owe.
print('This conversion will let you know how much each person has to pay when splitting a bill.')
total_bill=float(input('What is the total bill? '))
people_in_party=int(input('How many people are in your party? '))
individual_amount=total_bill/people_in_party
print(f'Each person will have to pay ${individual_amount:.2f}')
# I had to look up how to round to 2 decimal places, I didn't know how to do that. 