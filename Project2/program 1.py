#This program will calculate the tax on a purchase.
#It will also calculate the total cost of the purchase including tax.
#It will use if statements to determine the tax because it will change according to the purchase cost.

purchase_price=float(input('What is the cost of your purchase? '))
if purchase_price<50:
    tax=purchase_price*0.05
    total_price=purchase_price+tax
    print(f'Your tax is ${tax:.2f} and your total price is ${total_price:.2f}')
    #I used this .2f in the previous program is is a nice way to round 2 decimal places.
elif purchase_price<100: 
    #if the purchase price is not less that 50 then it will check if it is less than 100.
    tax=purchase_price*0.06
    total_price=purchase_price+tax
    print(f'Your tax is ${tax:.2f} and your total price is ${total_price:.2f}')
else:
    #if the purchase price is not less than 50 or 100 it will then calculate the tax at 7%
    tax=purchase_price*0.07
    total_price=purchase_price+tax
    print(f'Your tax is ${tax:.2f} and your total price is ${total_price:.2f}')

#It took me a minute to figure out if the previous less than would affect the next if statement.
