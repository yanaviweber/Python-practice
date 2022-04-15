# Ex 5.2

# 5.2.1

my_city = 'Leipzig'
print("Is your city is Leipzig? I predict it is true.")
if my_city == 'Leipzig':
    print("Yes, your city is Leipzig")
    print(my_city == 'Leipzig')
print("You variant is correct.")

print("\nIs your city is Drezden? I predict it is false.")
print(my_city == 'Drezden')
print("Your variant is no correct.")

print("\n-------------------------")

# Ex 5.2.2

my_live_country = 'Germany'
print("Is your country is Germany? I predict it is true.")
if my_live_country == 'Germany':
    print("Yes, your country is Germany")
print("You variant is correct.")

print("\nIs your country is Germany? I predict it is true.")
# print(my_live_country == 'Germany') --- this I have not to write because it is mistake variant!!!
print(my_live_country.lower() == 'germany')
print("Your variant it is correct.")
# Ex 5.2.3

my_cars = 5
print("\nDo you have 5 cars? I predict it is true.")
print(my_cars == 5)
print("Your answer is correct. You have 5 cars.")

print("\nDo you have >5 cars? I predict it is false.")
print(my_cars > 5)
print("Your answer is not correct. You don't have more 5 cars.")

print("\nDo you have <5 cars? I predict it is false.")
print(my_cars < 5)
print("Your answer is not correct. You don't have less 5 cars.")

print("\nDo you have 5 cars or more? I predict it is true.")
print(my_cars >= 5)
print(f"Your answer is correct. You have {my_cars} cars.")

print("\nDo you have 5 cars or less? I predict it is true.")
print(my_cars <= 5)
print(f"Your answer is correct. You have {my_cars} cars.")

# Ex 5.2.4

favorite_cat_food_first = 'chicken'
favorite_cat_food_second = 'fish'
if favorite_cat_food_first == 'chicken' and favorite_cat_food_second == 'fish':
    print("\nMarsik likes it a lot.")

all_favorite_cat_food = ['chicken', 'fish', 'beef']
if 'beef' in all_favorite_cat_food:
    print("\nMarsik likes this beef food, but it is not a lot.")

if 'vegetables' not in all_favorite_cat_food:
    print("\nThis food complex is good for Marsik.")

