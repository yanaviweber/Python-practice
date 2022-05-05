responses = {}

# set the value of the flag
polling_active = True

while polling_active:

    # request of user's name and answer
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # save of the answer in the dictionary
    responses[name] = response

    # check of the questionnaire continue
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# questionnaire completed, show results of this
print("\n-------- Poll Results --------")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
