user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print("\n---------------")
favorite_languages_for_users = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# ----- the main file with topic scripts with UNSORTED and SORTED array ------------

if 'erin' not in favorite_languages_for_users.keys():
    print("Erin, please take our poll!")

for name, language in favorite_languages_for_users.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages_for_users.keys():
    print(name.title())
print("\n-------------------------")
friends = ['phil', 'sarah']
for name in favorite_languages_for_users.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages_for_users[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
print("\n-------------------------")

for name in sorted(favorite_languages_for_users.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("\n-------------------------")

print("The following languages have been mentioned:")
for language in favorite_languages_for_users.values():
    print(language.title())

print("\n-------------------------")
print("The following languages have been mentioned(with using set):")
for language in set(favorite_languages_for_users.values()):
    print(language.title())
print("\n-------------------------")


