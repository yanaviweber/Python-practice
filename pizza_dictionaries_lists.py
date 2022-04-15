
# list in dictionary
# save data of the request of the selected pizza
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

# description of request
print(f"You ordered a {pizza['crust']} - crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

