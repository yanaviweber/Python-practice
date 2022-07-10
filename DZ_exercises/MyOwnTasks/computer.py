class Computer():
    """ Initialize all params of class """
    def __init__(self, brand, device_type, hard_disk_type, hard_disk_quantity, ram_quantity,
                 year_of_produce, age, owner_name):
        self.brand = brand
        self.device_type = device_type
        self.hard_disk_type = hard_disk_type
        self.hard_disk_quantity = hard_disk_quantity
        self.ram_quantity = ram_quantity
        self.year_of_produce = year_of_produce
        self.age = age
        self.owner_name = owner_name


    def describe_computer(self):
        """ Show all info of computer class  params """
        data_info = f"This computer has these params:\n" \
                    f"1) brand => {self.brand}\n" \
                    f"2) type of computer is => {self.device_type}\n" \
                    f"3) hard_disk_type => {self.hard_disk_type}\n" \
                    f"4) hard disk quantity => {self.hard_disk_quantity}\n" \
                    f"5) ram quantity => {self.ram_quantity}\n" \
                    f"6) year of produce => {self.year_of_produce}\n" \
                    f"7) age of computer => {self.age}\n" \
                    f"8) owner name is => {self.owner_name}\n"
        print(f"{data_info}")

    def produce_music(self):
        """ About functions with play audio """
        print("This function - 'Produce music' is enable and works good.")

    def enter_symbols_in_keyboard(self):
        """ About functions with keyboard """
        print("This function - 'Enter with keyboard' is enable and works good.")

    def sync_with_mouse(self):
        """ Mouse syncronization """
        print("This function - 'Mouse work clicks' is enable and works good.")

    def energy_concumpteon(self):
        """ Power modes """
        print("This function - 'Power mode' is enable and works good.")

my_computer = Computer("HP", "Laptop", "HDD", 250, 8, 2017, 5, "Viktoriia Romaniuk")
my_computer.describe_computer()
my_computer.energy_concumpteon()
my_computer.enter_symbols_in_keyboard()
my_computer.sync_with_mouse()
my_computer.produce_music()



# -------- Class My computer ------  CHILD class

class My_Computer(Computer):
    def __init__(self, brand, device_type, hard_disk_type, hard_disk_quantity, ram_quantity,
                 year_of_produce, age, owner_name):
        super().__init__(brand, device_type, hard_disk_type, hard_disk_quantity, ram_quantity,
                 year_of_produce, age, owner_name)

        self.camera = 1
        self.power_mode = 0

    def describe_camera(self):
        """ About camera in general in this device"""
        if self.camera == 1:
            print("Computer has a camera.")
        else:
            print("Camera not found.")


    def energy_concumpteon(self):
        """ Power mode in this model of device """
        if self.power_mode == 0:
            print("This device works from energy system")
        elif self.power_mode == 1:
            print("This device works from battery.")
        elif self.power_mode == 2:
            print("This device works in greedy mode.")
        elif self.power_mode == 3:
            print("This device works in sleepy mode.")
        else:
            print("This device turned.")

my_other_laptop = My_Computer("Apple", "Laptop", "SSD", 500, 16, 2021, 1, "Viktoriia Romaniuk")
my_other_laptop.describe_computer()
# print(f"{my_other_laptop.power_mode()}")
my_other_laptop.energy_concumpteon()
