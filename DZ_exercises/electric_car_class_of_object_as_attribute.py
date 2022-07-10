class Car():
    """ The model of car """

    def __init__(self, make, model, year):
        """ Params of model Car as explain it """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fill_gas_tank_value = 100


    def get_descriptive_name(self):
        """ Return clean formatting description of model name and other important info """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """ Show message about count km of miles """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """ Set value on the odometer
            When will try change this back, - it is not possible
        """
       # self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back an odometer!")

    def increment_odemeter(self, miles):
        """ Increase the values of odemeter c set of increasing value """
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """ Describe all information about gas tank in car """
        print(f"The minimum reguirement for driving car is {self.fill_gas_tank_value} litr.")


class Battery():
    """ Simple model of car battery """
    def __init__(self, battery_size=75):
        """ Initializing battery attributes """
        self.battery_size = battery_size

    def describe_battery(self):
        """ Show info about power of battery """
        print(f"This is a {self.battery_size}-kWh battery.")

    def get_range(self):
        """ Displays the approximate range for the battery """
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

# Ex. 9.9
    def upgrade_battery(self):
        """ Check size of battery and set value in 100 """
        if self.battery_size == 75:
            self.battery_size = 100
            print("Battery is upgraded to 100 kWH.")
        else:
            print(f"Battery size is already upgraded.")

class ElectricCar(Car):
    """ Describe the technic characteristics which has an electric car only """

    def __init__(self, make, model, year):
        """ Initialize attributes of parent class.
         After it is initializing attributes for only electric cars.
         """
        super().__init__(make, model, year)
        # self.battery_size = 75
        self.battery = Battery()  # class in attribute inside

    def fill_gas_tank(self):
        """ Electric cars dont have a gas tank """
        print("This car doesn't have a gas tank.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()

my_tesla.battery.get_range()

print("---------")
my_other_car = Car('Toyota', 'Camry', 2017)
my_other_car.fill_gas_tank()
print("---------")

# Ex. 9.9
print("---- START 9.9 -----")
my_audi_car = ElectricCar('audi', 'a6', 2017)
my_audi_car.battery.get_range()
my_audi_car.battery.upgrade_battery()
my_audi_car.battery.get_range()

print("---- END 9.9 -----")
