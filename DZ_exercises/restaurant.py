# Ex 9.1

class Restaurant():

    """ Class represent a restaurant """

    def __init__(self, restaurant_name, cuisine_type):
        """ The main params of restaurant """
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """ Show describe text of restaurant """
        message = f"Restaurant name is {self.restaurant_name}. The type - {self.cuisine_type}."
        print(message)


    def open_restaurant(self):
        """ Show info about Open/Close this restaurant """
        message = f"{self.restaurant_name} is open now."
        print(message)

    def set_number_served(self, number_served):
        """ Permit for change any count for the people in restaurant """
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """ Permit to set to increase this value for 1 """
        self.number_served += additional_served

restaurant = Restaurant('Barva', 'LUX-Restaurant')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("---------------")
print("\n")

print("-------START 9.4 Task-----------")
restaurant_9_4 = Restaurant('Viki Line', 'Italian cafe')
print(f"{restaurant_9_4.number_served}")

restaurant_9_4.describe_restaurant()

print(f"\nNumber served: {restaurant_9_4.number_served}")
restaurant_9_4.number_served = 250
print(f"Number served: {restaurant_9_4.number_served}")

restaurant_9_4.set_number_served(1000)
print(f"Number served: {restaurant_9_4.number_served}")

restaurant_9_4.increment_number_served(122)
print(f"Number served: {restaurant_9_4.number_served}")

# START -------- it is not right but it gets understanding what is correctly
# restaurant_9_4.set_number_served()
# restaurant_9_4.increment_number_served()
# print(f"{restaurant_9_4.number_served}")
# END ---------- not correctly decision
print("-------END 9.4 Task-----------")

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

# Ex. 9.6

class IceCreamStand(Restaurant):
    """ Describe a child class IceCreamStand """

    def __init__(self, restaurant_name, cuisine_type='ice_cream'):  # write type in value in cuisine_type
        """ Describe initialise params of child class """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []  # write type of data - array as a value of flavors


    def describe_flavors(self):
        """ Show information of method of flavors """
        print(f"This restaurant has some count of flavors.")
        for flavor in self.flavors:
            print(f"-  {flavor.title()}")

myIceCreamStand = IceCreamStand("Vivien cafe", "ice_cream")
myIceCreamStand.flavors = ["chocolate", "strawberry", "peach"]

myIceCreamStand.describe_restaurant()
myIceCreamStand.describe_flavors()


