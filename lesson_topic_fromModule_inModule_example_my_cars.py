from lesson_topic_fromModule_inModule_example_car import Car
from lesson_topic_fromModule_inModule_example_electric_car import ElectricCar
# using this as an alias
# from lesson_topic_fromModule_inModule_example_electric_car import EC


print("-----------------------------")
my_second_beetle = Car('volkswagen', 'beetle', 2022)
print(my_second_beetle.get_descriptive_name())

print("-----------------------------")
my_second_tesla = ElectricCar('tesla', 'model S', 2022)
print(my_second_tesla.get_descriptive_name())
# using this as an alias
# my_second_tesla = EC('tesla', 'model S', 2022)
