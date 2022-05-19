pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


# ------ Functions --------------

def describe_pet(animal_type, pet_name):
    """ To show information about pet """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')

describe_pet('cat', 'marsik')
describe_pet(animal_type="rabbit", pet_name="java")

# Case about if a lot of pets (more then 50%) are only dogs, we set as default "dog" as a type of animal
def describe_pet_3(pet_name, animal_type = 'dog'):
    """ Show info about animal """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet_3(pet_name='willie')

describe_pet_3('wilie')

describe_pet_3('harry', 'hamster')
describe_pet_3(pet_name='harry', animal_type='hamster')
describe_pet_3(animal_type='hamster', pet_name='harry')


