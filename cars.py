# sort() function
cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()
print(cars)

# sort with "reverse=True" parameter
cars_second_reverse = ['bmw', 'audi', 'toyota', 'subaru']
cars_second_reverse.sort(reverse=True)
print(cars_second_reverse)

# sorted() function
cars_third = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars_third)

print("\nHere is the sorted list:")
print(sorted(cars_third))

print("\nHere is the original list again:")
print(cars_third)

# reverse() function
cars_third.reverse()
print(cars_third)

# if-else intructions chapter
cars_fourth = ['bmw', 'audi', 'toyota', 'subaru']
for f_car in cars_fourth:
    if f_car == 'bmw':
        print(f_car.upper())
    else:
        print(f_car.title())

