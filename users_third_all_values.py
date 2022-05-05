favorite_languages_third = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# ----- the other try in other file with operations with UNSORTED array ------------

print("The following languages have been mentioned:")
for language in favorite_languages_third.values():
    print(language.title())

print("\nThe following languages have been mentioned with using set:")
for language in set(favorite_languages_third.values()):
    print(language.title())
