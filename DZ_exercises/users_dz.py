# Ex. 5.8

users_list = ['Vika', 'Sveta', 'andreas', 'admin', 'kefi']
for user in users_list:
    if user == 'admin':
        print(f"Hello, admin, would you like to see a status report?")
    else:
        print(f"Hello, {user}, thank you for logging in again.")
print("\n___________________________________")
# Ex 5.9

# myMother_users_list = ['Vika', 'Liubov', 'Slavik', 'admin', 'Sveta']
myMother_users_list = []
if myMother_users_list:
    for user in users_list:
        if user == 'admin':
            print(f"Hello, admin, would you like to see a status report?")
        else:
            print(f"Hello, {user}, thank you for logging in again.")
else:
    print("Your list of users is empty.")
print("\n___________________________________")
# Ex 5.10

current_users = ['Tania', 'Viktor', 'Sveta', 'Liubov', 'Mars', 'Simon', 'Anni']
new_users = ['Viktor', 'Alina', 'MARS', 'Jane', 'Andrew']
# its CREATING EFFECTIVELY DECISION start
current_users_lower = [user.lower() for user in current_users]
# its CREATING EFFECTIVELY DECISION end
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user}, you are have to create another name.")
    else:
        print(f"{new_user}, your name is OK in the system.")

print("\n___________________________________")
# Ex 5.11

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number_example in number_list:
    if number_example == 1:
        print(f"It is a {number_example}st.")
    elif number_example == 2:
        print(f"It is a {number_example}nd.")
    elif number_example == 3:
        print(f"It is a {number_example}rd.")
    else:
        print(f"It is a {number_example}th.")




