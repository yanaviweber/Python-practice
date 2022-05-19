def build_person(first_name, last_name, age=None):
    """ Return a dictionary with data about person """
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('Marsik', 'Romaniuk', age=7)
print(musician)
