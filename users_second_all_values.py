favorite_languages_second = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# ----- the other try in other file with operations with SORTED array ------------

for name in sorted(favorite_languages_second.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
#    print(favorite_languages_second)
print("\n-------------------")
for language in sorted(favorite_languages_second.values()):
    print(f"{language.title()}, thank you for taking the poll.")
#    print(favorite_languages_second)
print("\n-------------------")
print("The following languages have been mentioned:")
for language in favorite_languages_second.values():
    print(language.title())

print("\nThe following languages have been mentioned with using set:")
for language in set(favorite_languages_second.values()):
    print(language.title())

