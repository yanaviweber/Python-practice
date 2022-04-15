# Ex. 6.1
people = []
human = {
    'first_name': 'Viktoriia',
    'last_name': 'Romaniuk',
    'age': 30,
    'city': 'Leipzig',
}
print(f"\nFirst name is: {human['first_name']}.")
print(f"LAst name is: {human['last_name']}.")
print(f"Age is: {human['age']}.")
print(f"City is: {human['city']}.\n")

# Ex.6.2
favorite_numbers = {
    'Sveta': 7,
    'Vika': 7,
    'Tania': 5,
    'Andrew': 24,
    'Stas': 101,
}

print(f"Favorite number of Sveta is: {favorite_numbers['Sveta']}.")
print(f"Favorite number of Vika is: {favorite_numbers['Vika']}.")
print(f"Favorite number of Tania is: {favorite_numbers['Tania']}.")
print(f"Favorite number of Andrew is: {favorite_numbers['Andrew']}.")
print(f"Favorite number of Stas is: {favorite_numbers['Stas']}.")

# Ex 6.3

glossary = {
    'Python': 'Language for programming',
    'strip()': 'It is operation for deleting empty area in the line with left and right near the word',
    'title()': 'It is operation for transform the first letter of every word as a big letter',
    'for': 'It is a type of cycles',
    'lower()': 'It is the operation for transform all letters in the word as small',
}
print(f"Python is: - {glossary['Python']}.")
print(f"Function strip() is: - {glossary['strip()']}.")
print(f"Function title() is: - {glossary['title()']}.")
print(f"Cycle \"for\" is: - {glossary['for']}.")
print(f"Function lower() is: - {glossary['lower()']}.")

print("\n------------------------------------------")
# Ex 6.4

for key, value in glossary.items():
    print(f"{key.title()} ---> {value.lower()}.")

print("\n------------------------------------------")
print("The Second Variand of glossary with adding new elements:--------")
glossary['PyCharm'] = 'it is a development tool for creating code in Python.'
glossary['set()'] = 'It is a function for dictionary when we look the same values.'
glossary['items()'] = 'It is function with dictionary when we show all elements through \'for\'.'
glossary['sort()'] = 'It is a function for sorting for dictionaries.'
glossary['value(), key()'] = 'It is a functions which helped us to show elements in dictionary when we use \'for\'.'
for key, value in glossary.items():
    print(f"{key.title()} ---> {value.lower()}.")

print("\n------------------------------------------")

# Ex 6.5

rivers = {
    'nile': 'egypt',
    'dnipro': 'ukraine',
    'rein': 'germany',
}
print("------- Explain about names of river and names of country.-------")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print("\n------- Explain about names of river.-------")
print("The list of rivers:")
for river in rivers.keys():
    print(f"{river.title()}.")

print("\n------- Explain about names of country.-------")
print("The list of countries of the rivers:")
for country in rivers.values():
    print(f"{country.title()}.")

print("\n------------------------------------------")
# Ex 6.6

myFriend_favourite_languages = {
    'anton': 'swift',
    'kirill': 'python',
    'vova': 'java',
    'alexandr': 'python',
    'alexey': 'swift',
    'mahmud': 'javascript',
}
for name, language in myFriend_favourite_languages.items():
    print("What is your favorite language?")
    print(f"{name.title()} likes language {language.title()} in his work.")

myFriend_favourite_languages['alexandr'] = 'swift'
myFriend_favourite_languages['alexey'] = 'go'
myFriend_favourite_languages['roman'] = 'ruby'

# It's not right decision ----------------
# for name, language in myFriend_favourite_languages.items():
#    if name in myFriend_favourite_languages:
#        print("Good, Let's go to coding!")
#    else:
#        print(f"{name.title()}, Welcome to us! You like a {language.title()}.")


# It's right decision ---------------------
other_developers = ['alexandr', 'slavik', 'alexey', 'piter', 'nikolas', 'roman']
for other_developer in other_developers:
    if other_developer in myFriend_favourite_languages:
        print(f"{other_developer.title()} - Let's go!")
    else:
        print(f"{other_developer.title()}, Welcome for us!")

print("\n-------------------------------------------")
# Ex 6.7

mother = {
    'first_name': 'Svitlana',
    'last_name': 'Romaniuk',
    'age': 50,
    'city': 'Leipzig',
}

father = {
    'first_name': 'Andrii',
    'last_name': 'Romaniuk',
    'age': 57,
    'city': 'Lviv',
}

people.append(human)
people.append(mother)
people.append(father)

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = f"{person['age']}"
    city = f"{person['city'].title()}"

    print(f"This person -- {name}, has {age} years old, and lives in {city}. Welcome!")

print("\n-------------------------------------------")

# Ex 6.8

pets = []

marsik = {
    'type': 'cat',
    'location_of_born': 'ukraine',
    'color': 'orange',
    'owners_name': 'vika',
}

fritzi = {
    'type': 'cat',
    'location_of_born': 'germany',
    'color': 'white-black',
    'owners_name': 'street',
}

javochka = {
    'type': 'rabbit',
    'location_of_born': 'ukraine',
    'color': 'orange-white',
    'owners_name': 'vika',
}

pets.append(marsik)
pets.append(fritzi)
pets.append(javochka)

for pet in pets:
    type = f"{pet['type'].title()}"
    location = f"{pet['location_of_born'].title()}"
    color = f"{pet['color'].title()}"
    owners_name = f"{pet['owners_name'].title()}"

    print(f"This pet has: \n\ttype is -> {type}, \n\tlocation of born is -> {location}, \
    \n\tcolor is -> {color}, \n\towner is -> {owners_name}")


print("\n-------------------------------------------")

# Ex 6.9

favorite_places = {
    'me': ['Leipzig', 'Praha', 'Kiev'],
    'mother': ['Kiev'],
    'marsik': ['home', 'garden'],
}

for name, places_info in favorite_places.items():
    print(f"The person {name.title()} likes this places:")
    for place in places_info:
        print(f"\t{place.title()}.")

print("\n-------------------------------------------")

# Ex 6.10
favorite_numbers_a_lot_of_numbers = {
    'Sveta': [7, 555],
    'Vika': [777, 7, 1111],
    'Tania': [22, 5, 101, 333],
    'Andrew': [24],
    'Stas': [101, 8],
}

for person_name, person_numbers in favorite_numbers_a_lot_of_numbers.items():
    print(f"Person {person_name.title()} likes this numbers:")
    for number in person_numbers:
        print(f"{number}.")

print("\n-------------------------------------------")

# Ex 6.11

cities = {
    'kiev': {
        'country': 'ukraine',
        'population': 10000000,
        'fact': 'the capital of Ukraine'
    },
    'london': {
        'country': 'great britain',
        'population': 1570000,
        'fact': 'the capital of Great Britain'
    },
    'leipzig': {
        'country': 'germany',
        'population': 568000,
        'fact': 'the best education area in Germany'
    },
}

for name_of_city, info_of_city in cities.items():
    print(f"\nThe city {name_of_city.title()} has:")
    country = f"{info_of_city['country'].title()}"
    population = f"{info_of_city['population']}"
    fact = f"{info_of_city['fact'].title()}"

    print(f"\tName of the country: --> {country}, \n\tCity population is: --> {population}, \n\tFact of city: --> {fact}.")

print("\n-------------------------------------------")

