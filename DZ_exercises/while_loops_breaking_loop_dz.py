# Ex 7.4
toppings = "\nPlease, enter your answer to 'What topping do you want in your pizza?'"
toppings += "\nEnter 'quit' if you would like to cancel program: "

while True:
    pizza = input(toppings)

    if pizza == 'quit':
        break
    else:
        print(f"We are added your {pizza} in your pizza.")

# Ex 7.5 - 7.6

price_ticket = 0

user_age = "\nPlease, enter your age:"
user_age += "\n(Enter 'quit' when you are finished) "

while True:
    user = input(user_age)
    if user == 'quit':
        break

    user = int(user)

    if user <= 3:
        price_ticket = 0
        print("You can go free to our cinema.")
    elif user <= 12:
        price_ticket = 10
        print(f"You have to price {price_ticket} USD to entrance in our cinema.")
    elif user > 12:
        price_ticket = 15
        print(f"You have to price {price_ticket} USD to entrance in our cinema.")


