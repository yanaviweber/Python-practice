# Ex 9.3

class User():
    def __init__(self, first_name, last_name, eyes_color, height, city):
        """ Show all info about object User """
        self.first_name = first_name
        self.last_name = last_name
        self.eyes_color = eyes_color
        self.height = height
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        """ Show info about describe text of user """
        print(f"This user with name: {self.first_name} {self.last_name}. \n"
              f"Also this user has {self.eyes_color} of eyes, {self.height} of the person height. \n"
              f"This person has location {self.city} of living.")

    def greet_user(self):
        """ Show info about hello text for user individual """
        print(f"Hello, dear {self.first_name} {self.last_name}! You have cool look and you are perfect person!")

    def increment_login_attempts(self):
        """ Increment login_attempts in 1 """
        self.login_attempts += 1

    def reset_login_attempts(self):
        """ Delete all params of login_attempts"""
        self.login_attempts = 0

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

print("START----------- 9.5 ------------")
my_laptop = User("Asus", "Testov", 'black', 0.3, 'Berlin')

my_laptop.describe_user()
my_laptop.greet_user()


print("Call 3 times an increment function")
my_laptop.increment_login_attempts()
my_laptop.increment_login_attempts()
my_laptop.increment_login_attempts()
print(f"Login attempts: {my_laptop.login_attempts}")

print("Reset all params of login attempts function")
my_laptop.reset_login_attempts()
print(f"Login attempts: {my_laptop.login_attempts}")

my_laptop.describe_user()

print("END----------- 9.5 ------------")


# Ex. 9.8

class Privileges():
    """ Model of privileges of users """
    def __init__(self):
        """ Show list of privileges """
        self.privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей"]

    def show_privileges(self):
        """ Show some privileges in print type """
        print("This user has these privileges:")
        for privilege in self.privileges:
            print(f"-  {privilege}")


# Ex. 9.7
class Admin(User):
    def __init__(self, first_name, last_name, eyes_color, height, city):
        """ Initialize attributes of parent for child class Admin"""

        super().__init__(first_name, last_name, eyes_color, height, city)
#        self.privileges = []
        """ Privileges ss an object in attribute of class """
        self.privileges = Privileges()


#    def show_privileges(self):
#        """ Show some privileges in print type """
#        print("This user has these privileges:")
#        for privilege in self.privileges:
#            print(f"-  {privilege}")


myAdminUser = Admin("Viktoriia", "Romaniuk", "grey-green", 1.65, "Leipzig")
myAdminUser.privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей",
                          "разрешено банить пользователей"]

myAdminUser.describe_user()
# myAdminUser.show_privileges()
print(" START ----------- 9.8 ------------")

myNewAdminUser = Admin("Svitlana", "Romaniuk", "grey-green", 1.67, "Leipzig")
myNewAdminUser.describe_user()
myNewAdminUser.privileges.show_privileges()

print(" END ----------- 9.8 ------------")
