favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

# for name, languages in favorite_languages.items():
#    print(f"\n{name.title()}'s favorite languages are:")
#    for language in languages:
#        print(f"\t{language.title()}")

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"{name.title()} language is C.")


