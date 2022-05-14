# Ex 8.1

def display_message():
    """ Show message on the display """
    print("This topic about functions.")
display_message()

# Ex 8.2
my_favorite_book = input("What is the Author and Name of your favorite book? ")

def favorite_book(my_favorite_book):
    print(f"Your favorite book is {my_favorite_book.title()}.")
favorite_book(my_favorite_book)

# Ex 8.3

shirt_size = input("Please, tel me, what is size of your shirt? (in number)")
shirt_text = input("What text would do you like on your shirt? ")
shirt_size_int = int(shirt_size)

def make_shirt(size, text):
    """ Show size of the shirt """
    print(f"Your variant: {text}.")
    print(f"Your shirt is {size}.")
make_shirt(shirt_size_int, shirt_text)

# Ex 8.4

def make_shirt_large(size='L', text='I love Python'):
    """ Show size of the shirt """
    print(f"This shirt has {size}.")
    print(f"Text on this shirt - {text}.")

make_shirt_large()

make_shirt_large(size='M')
make_shirt_large(text='I like LINUX a lot')

# Ex 8.5

def describe_city(city_name='Reykjavik', country_name='Iceland'):
    """ Show datain message """
    show_message = f"{city_name.title()} is in {country_name.title()}."
    print(show_message)

describe_city(city_name='London', country_name='Great Britain')
describe_city(city_name='San-Francisco', country_name='USA')
describe_city(city_name='Borgarnes')
describe_city(city_name='Agilsstadir')

# Ex 8.6
def city_country(name_of_the_city, name_of_the_country):
    print(f"{name_of_the_city.title(), name_of_the_country.title()}")

city_country('leipzig', 'germany')
city_country('lviv', 'ukraine')
city_country('san-francisco', 'usa')

# Ex 8.7

