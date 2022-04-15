import loops_dz
import foods
# Ex 4.3
for item in range(1, 21):
    print(item)

# Ex 4.4
one_million = range(1, 1000001)
# for number in one_million:
#    print(number, end=" ")
print("\n")

# Ex 4.5
min_of_million = min(one_million)
max_of_million = max(one_million)
print(f"Minimum in the million: {min_of_million}, \
 \nMaximum in the million: {max_of_million}.")
sum_of_million = sum(one_million)
print(f"Sum in one million numbers is: {sum_of_million}")

# Ex 4.6
list_test = range(1, 21, 2)
for test_number in list_test:
    print(test_number)

# Ex 4.7
divisible_by_three = range(3, 30, 3)
for number in divisible_by_three:
    print(number)

# Ex 4.8
kub_list = []
for item in range(1, 10):
    kub = item ** 3
    kub_list.append(kub)
print(kub_list)

# Ex 4.9
generated_kub_list = [kub_example**3 for kub_example in range(1, 10)]
print(generated_kub_list)

# Ex 4.10
my_computers = ['Macbook Pro', 'Asus', 'Hewlett-Packard', 'Dell', 'Lenovo', 'Acer', 'E-machine']
print(f"My computers are: \n{my_computers} \n")
print("The first three items in the list are: ")
print(f"{my_computers[:3]}\n")

print("Three items from the middle of the list are:")
print(f"{my_computers[2:5]}\n")

print(f"The last three items in the list are:")
print(f"{my_computers[-3:]}\n")

# Ex 4.11

friend_pizzas = loops_dz.my_favourite_pizzes[:]
loops_dz.my_favourite_pizzes.append('diavola')
friend_pizzas.append('credizemnomorskaia')
print(f"My favorite pizzas are:")
for my_favorite_pizza in loops_dz.my_favourite_pizzes:
    print(my_favorite_pizza)
print("\n")

print(f"My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
print("\n")

# Ex 4.12
copy_my_food = foods.my_foods[:]
print("My favorite dishes are:")
for dish in copy_my_food:
    print(dish)
print("\n")


copy_friend_food = foods.friend_foods[:]
print("Friend's favorite dishes are:")
for dish in copy_friend_food:
    print(dish)
print("\n")
