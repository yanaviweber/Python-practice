""" Set of classes for presenting electro cars """
# from fromModule_inModule_example-car import Car

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


# Class Electric Car -------------------------------

class ElectricCar(Car):
    """ Describe the technic characteristics which has an electric car only """

    def __init__(self, make, model, year):
        """ Initialize attributes of parent class.
         After it is initializing attributes for only electric cars.
         """
        super().__init__(make, model, year)
        self.battery = Battery()