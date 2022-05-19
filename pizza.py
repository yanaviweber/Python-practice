def make_pizza(*toppings):
    """ Show list of all toppings """
    print(toppings)

make_pizza('peperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_my_pizza(size, *my_toppings):
    """ Show the explain of pizza """
    print(f"\nMaking a {size}-inch pizza with the following toppings.")
    for my_topping in my_toppings:
        print(f"- {my_topping}")


