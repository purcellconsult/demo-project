#######################################
# Grocery budget
# --------------
#
# A simple script that simulates
# grocery shopping. User selects
# what items they want and what quantity.
# The script will compare user budget to the
# the total grocery bill.
# If user has budget the program will return the change.
# Otherwise the program will tell the user that they don't
# have enough money.
#
# items:
# ------
# milk == 5.00
# bread == 3.50
# eggs == 4.00
# cheese == 8.00
#
# budget
# ------
# randomly assigned
#
#########################################

import random

print("""
 milk = $5
 bread = $3.50
 eggs = $4
 cheese = $8.00
""")

budget = random.randint(1, 100)  # randomly assigns budget
print('You budget is ${}'.format(budget))
milk, bread, eggs, cheese = 5, 3.50, 4, 8
milk_cost = int(input('Enter in quantity of milk '))
if milk_cost < 0:
    exit('Invalid amount. Program terminating...')
else:
    milk_cost = milk * milk_cost
bread_cost = int(input('Enter in quantity of bread '))
if bread_cost < 0:
    exit('Invalid amount. Program terminating...')
else:
    bread_cost = bread * bread_cost
egg_cost = int(input('Enter in quantity of eggs '))
if egg_cost < 0:
    exit('Invalid amount. Program terminating...')
else:
    egg_cost = eggs * egg_cost
cheese_cost = int(input('Enter in quantity of cheese '))
if cheese_cost < 0:
    exit('Invalid amount. Program terminating...')
else:
    cheese_cost = cheese * cheese_cost

grocery_bill = milk_cost + bread_cost + egg_cost + cheese_cost
print('The total grocery bill is ${}'.format(grocery_bill))
print('Your budget is ${}'.format(budget))
if grocery_bill > budget:
    print('You\'re short ${} :-('.format(grocery_bill - budget))
else:
    print('Your change ${}'.format(budget - grocery_bill))

