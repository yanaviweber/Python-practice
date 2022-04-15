requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")
print("\n-------------------------------")
print("---Searching with \"if\" in the list.---")
my_favorite_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in my_favorite_toppings:
    print("Adding mushrooms.")
if 'peperoni' in my_favorite_toppings:
    print("Adding peperoni.")
if 'extra cheese' in my_favorite_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
print("\n-------------------------------")
print("---Searching with \"for\" in \"Is this element in list or not?\".---")
myMother_favorite_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for myMother_favorite_topping in myMother_favorite_toppings:
    if myMother_favorite_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {myMother_favorite_topping}.")

print("\nFinished making your's mother pizza!")
print("\n-------------------------------")
print("---Searching with \"for\" in empty list.---")
myFriend_favorite_toppings = []
if myFriend_favorite_toppings:
    for myFriend_favorite_topping in myFriend_favorite_toppings:
        print(f"Adding {myFriend_favorite_topping}.")
    print("\nFinished making my friend's pizza!")
else:
    print("\nAre you sure want a plain pizza?")

print("\n-------------------------------")
print("---Searching with \"for\" in the list in list.---")

secondPizza_available_toppings = ['mushrooms', 'olives', 'green peppers',
                                  'peperoni', 'pineapple', 'extra cheese']
myBrother_requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for myBrother_requested_topping in myBrother_requested_toppings:
    if myBrother_requested_topping in secondPizza_available_toppings:
        print(f"Adding {myBrother_requested_topping}.")
    else:
        print(f"Sorry, we don't have {myBrother_requested_topping}.")
print("\nFinished making your pizza!")
