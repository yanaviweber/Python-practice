# Ex 9.1

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        """ The main params of restaurant """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """ Show describe text of restaurant """
        print(f"Restaurant name is {self.restaurant_name}. The type - {self.cuisine_type}.")


    def open_restaurant(self):
        """ Show info about Open/Close this restaurant """
        print(f"{self.restaurant_name} is open now.")

restaurant = Restaurant('Barva', 'LUX-Restaurant')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("---------------")
print("\n")

# Ex 9.2

myMom_restaurant = Restaurant('Romashka', 'bakery')
myMom_restaurant.describe_restaurant()
myMom_restaurant.open_restaurant()
print("---------------")

Olex_restaurant = Restaurant('Olex cafe', 'grill_restaurant')
Olex_restaurant.describe_restaurant()
Olex_restaurant.open_restaurant()
print("---------------")

Ines_restaurant = Restaurant('Ines Garden Cafe', 'bakery')
Ines_restaurant.describe_restaurant()
Ines_restaurant.open_restaurant()

