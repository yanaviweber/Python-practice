# Ex. 7.8
sandwich_orders = ['gamburger', 'cheesburger', 'bigmak', 'fishroyal']
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich")

while sandwich_orders:

    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)

print(f"We are made: {[finished_sandwiches[0]]}")


# Ex. 7.9
sandwich_orders_second = ['pastrami', 'gamburger', 'pastrami', 'cheesburger', 'pastrami', 'bigmak', 'fishroyal', 'pastrami']
finished_sandwiches_second = []

print("We have not pastrami")
while 'pastrami' in sandwich_orders_second:
    sandwich_orders_second.remove('pastrami')
print("We have these sandwiches:")
for sandwich in sandwich_orders_second:
    print(f"    {sandwich}")

# Ex. 7.10

dream_question = input("Enter please, Where is place for your holiday of your dream:")
print(f"Your dream holiday place is {dream_question}")

# second variant of 7.10

name_prompt = "\nWhat is your name?"
place_prompt = "What is you place which as your dream?"
continue_prompt = "\nWould like to let someone else respond? (yes / no) "

responses = {}

while True:
    name = input(name_prompt)
    place = input(place_prompt)

    responses[name] = place

    repeat = input(continue_prompt)
    if repeat != "yes":
        break

print("\n------------ Results --------------")

for name, response in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")



