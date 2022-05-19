def get_formatted_name(first_name, last_name):
    """ Return clean formatting full name """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimmi', 'hendrix')
print(musician)


# the function with additional params
def get_formatted_name_additional_params(first_name, last_name, middle_name=''):
    """ Return clean formatting full name """
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician_additional = get_formatted_name_additional_params('john', 'hooker', 'lee')
print(musician_additional)

musician_additional = get_formatted_name_additional_params('viktoriia', 'romaniuk')
print(musician_additional)

