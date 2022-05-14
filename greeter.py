user_name = input("Please enter your user name: ")
print(f"\nHello, {user_name}!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
first_name = input(prompt)
print(f"\nHello, {first_name}!")

age = input("How old are you? ")
print(f"Your age is {age} years old.")


# ------ Functions --------------

def greet_user():
    """ show only message """

    print("Hello!")

greet_user()


def great_user_2(first_name):
    """ Show message with name of user"""
    print(f"Hello, {first_name.title()}.")

great_user_2(first_name)


