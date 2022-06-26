class Car():
    """ The model of car """

    def __init__(self, make, model, year):
        """ Params of model Car as explain it """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


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


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

# change parameter with change this in class
# my_new_car.odometer_reading = 23

# change value with using method way which created in the class
my_new_car.update_odometer(23)

my_new_car.read_odometer()


my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odemeter(100)
my_used_car.read_odometer()

