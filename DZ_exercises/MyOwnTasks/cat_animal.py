# my own class Cat

class Cat():
    """ General class of all cats """
    def __init__(self, name, color, type, age, location, owner_name):
        self.name = name
        self.color = color
        self.type = type
        self.age = age
        self.location = location
        self.owner_name = owner_name
        self.food_monday_tuesday = ""
        self.food_wednesday_thursday = ""
        self.food_friday = ""
        self.food_saturday_sunday = ""
        self.favorite_food = ""
        self.behavior_in_the_morning = ""
        self.behavior_until_all_day = ""
        self.behavior_night = ""
        self.food_weight_in_day = 100
        self.food_drink_weight_in_day = 30


    def describe_cat(self):
        """ This shows info about some cat """
        data_info = f"\n-- name -> {self.name},\n-- color -> {self.color}," \
                    f"\n-- type -> {self.type},\n-- age -> {self.age}," \
                    f"\n-- location -> {self.location},\n-- owner name -> {self.owner_name}"
        print(f"This cat has: {data_info}")

    def eat_food(self):
        """ This shows data about what food in which days as a schedule can eat cat """
        print(f"Cat {self.name} eats food: \n"
              f"in Monday, Tuesday - {self.food_monday_tuesday}\n"
              f"in Wednesday, Thursday - {self.food_wednesday_thursday}\n"
              f"in Friday - {self.food_friday}\n"
              f"in Saturday, Wednesday - {self.food_saturday_sunday}\n")

    def quantity_of_food_in_day(self):
        """ Show all info about quantity of food and drink for one cat """
        data_info = f"This cat {self.name} eats these food in:\n" \
                    f"drink water - {self.food_drink_weight_in_day}ml in  a day,\n" \
                    f"eats food - {self.food_weight_in_day} gram in a day.\n"
        return data_info

    def describe_favourite_food(self):
        """ This shows data about favorite food of cat """
        data_info = f"Cat {self.name} likes a lot this food: {self.favorite_food}"
        return data_info

    def describe_behavior(self):
        """ This shows data about behavior of cat """
        data_info = f"Cat {self.name} does these actions:\n" \
                    f"-- in the morning -> {self.behavior_in_the_morning}\n" \
                    f"-- until all day include evening -> {self.behavior_until_all_day}\n" \
                    f"-- in the night -> {self.behavior_night}\n"
        return data_info

    def update_quantity_food(self, update_data_weight):

        if update_data_weight < 30:
            print("You are don't have change of this!!!")
        elif update_data_weight >= 30 and update_data_weight <= 70:
            self.food_weight_in_day = update_data_weight
            print("This is possible.")
        else:
            print("This is not possible for cat!!")

    def update_quantity_drink(self, update_data_drink):

        if update_data_drink < 100:
            print("You are don't have change of this!!!")
        elif update_data_drink >= 100 and update_data_drink <= 200:
            self.food_weight_in_day = update_data_drink
            print("This is possible.")
        else:
            print("This is not possible for cat!!")



my_cat = Cat("Fritzi", "white-black", "home cat", 5, "Leipzig", "Ines Witt")
my_cat.describe_cat()
my_cat.eat_food()

# ------ Class Marsik ----- CHILD class

# information in class only of my Marsik

class Marsik(Cat):
    """ It gets all attributes of parent class """
    def __init__(self, name, color, type, age, location, owner_name):
        super().__init__(name, color, type, age, location, owner_name)

        self.food_monday_tuesday = "chicken"
        self.food_wednesday_thursday = "beef"
        self.food_friday = "salmon"
        self.food_saturday_sunday = "chicken"

    def eat_food(self):
        """ This shows data about what food in which days as a schedule can eat Marsik """
        print(f"Cat {self.name} eats food: \n"
              f"in Monday, Tuesday - {self.food_monday_tuesday}\n"
              f"in Wednesday, Thursday - {self.food_wednesday_thursday}\n"
              f"in Friday - {self.food_friday}\n"
              f"in Saturday, Wednesday - {self.food_saturday_sunday}\n")

marsik_cat = Marsik("Marsik", "orange", "home cat", 7, "Leipzig", "Viktoriia Romaniuk")
marsik_cat.describe_cat()
marsik_cat.eat_food()

# marsik_cat.eat_food()
