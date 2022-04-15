# Ex. 5.3
alien_color = 'green'
if alien_color == 'green':
    print("You have 5 numbers now in alien_color.")

if alien_color != 'green':
    print("You have not 5 numbers now in alien_color_2.")

# Ex. 5.4

my_color = 'orange'
if my_color == 'orange':
    print("You have 5 numbers now in my_color.")
if my_color != 'orange':
    print("You have not 5 numbers in my_color.")

my_color_second = 'deep blue'
if my_color_second == 'deep blue':
    print("You have 5 numbers now. in my_color_second")
else:
    print("You have not 5 numbers in my_color_second.")

# Ex 5.5:

alien_color_some_version = 'green'
if alien_color_some_version == 'green':
    print("You have 5 numbers now in alien_color_some_version.")
elif alien_color_some_version == 'yellow':
    print("You have 10 numbers now in alien_color_some_version.")
elif alien_color_some_version == 'red':
    print("You have 15 numbers now in alien_color_some_version.")
else:
    print("You have other color. It is not correct.")

# Ex 5.6:

age_of_person = 25
if age_of_person < 2:
    print("You are baby.")
elif (age_of_person >= 2) and (age_of_person < 13):
    print("You are child.")
elif (age_of_person >= 13) and (age_of_person < 20):
    print("You are teenager.")
elif (age_of_person >= 20) and (age_of_person < 65):
    print("You are adult person.")
elif age_of_person >= 65:
    print("You are pensioner.")
else:
    print("It is not correctly value.")


# Ex 5.7:

favorite_fruits = ['pear', 'nektarine', 'mandarine']
if 'pear' in favorite_fruits:
    print("You are really like pears!")
if 'nektarine' in favorite_fruits:
    print("You are really like nektarines!")
if 'mandarine' in favorite_fruits:
    print("You are really like mandarines!")
if 'kiwi' in favorite_fruits:
    print("You are really like kiwi!")
if 'apple' in favorite_fruits:
    print("You are really like apples!")
