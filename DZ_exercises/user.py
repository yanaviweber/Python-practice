# Ex 9.3

class User():
    def __init__(self, first_name, last_name, eyes_color, height, city):
        """ Show all info about object User """
        self.first_name = first_name
        self.last_name = last_name
        self.eyes_color = eyes_color
        self.height = height
        self.city = city

    def describe_user(self):
        """ Show info about describe text of user """
        print(f"This user with name: {self.first_name} {self.last_name}. \n"
              f"Also this user has {self.eyes_color} of eyes, {self.height} of the person height. \n"
              f"This person has location {self.city} of living.")

    def greet_user(self):
        """ Show info about hello text for user individual """
        print(f"Hello, dear {self.first_name} {self.last_name}! You have cool look and you are perfect person!")

my_mother = User('Svitlana', 'Romaniuk', 'grey', 1.65, 'Leipzig')
my_mother.describe_user()
my_mother.greet_user()
print("---------------")

my_personal = User('Viktoriia', 'Romaniuk', 'grey', 1.65, 'Leipzig')
my_personal.describe_user()
my_personal.greet_user()
print("---------------")

my_friend = User('Oleksandr-Yuriy', 'Voychuk', 'gold brown', 1.84, 'Leipzig')
my_friend.describe_user()
my_friend.greet_user()

