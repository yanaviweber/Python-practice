class Dog():
    """ The example of Dog modes as object """

    def __init__(self, name, age):
        """ Initialize attributes name and age """
        self.name = name
        self.age = age

    def sit(self):
        """ Function about the dog is sit down when the host does the command to it """
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """ Function about the dog is rollover when the host does the command to it """
        print(f"{self.name} rolled over!")

my_dog = Dog('willie', 6)
your_dog = Dog('licy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age} years old.")



my_dog.name()
my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"\nYour dog is {your_dog.age} years old.")
your_dog.sit()


