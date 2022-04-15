# Ex 3.4
my_guests = ['Julia', 'Slavik', 'Luba']
print(f"Hi, {my_guests[0]}. Welcome!")
print(f"Hi, {my_guests[1]}. Welcome!")
print(f"Hi, {my_guests[2]}. Welcome!")

# Ex 3.5
print(f"Hi! {my_guests[2]} will absent tomorrow.")
my_guests[2] = 'Jana'
print(f"Hi, {my_guests[0]}. Welcome! We will have a new guest tomorrow!")
print(f"Hi, {my_guests[1]}. Welcome! We will have a new guest tomorrow!")
print(f"Hi, {my_guests[2]}. Welcome! We glad to see you!")

# Ex 3.6
# Preconditions: data of the Ex 3.4
print(f"Hi, {my_guests[0]}, {my_guests[1]}, {my_guests[2]}. We will add some guests in our team")

my_guests.insert(0, 'Aleksandr')
my_guests.insert(2, 'Ada')
my_guests.append('Steve')
print(f"Hi, {my_guests[0]}. Welcome! We updated our team.")
print(f"Hi, {my_guests[1]}. Welcome! We updated our team.")
print(f"Hi, {my_guests[2]}. Welcome! We updated our team.")
print(f"Hi, {my_guests[3]}. Welcome! We updated our team.")
print(f"Hi, {my_guests[4]}. Welcome! We updated our team.")
print(f"Hi, {my_guests[5]}. Welcome! We updated our team.")

# Ex 3.7
# Preconditions: data of the Ex 3.6
print(f"Hi! {my_guests[0]}, {my_guests[1]}, {my_guests[2]}, {my_guests[3]},\
 {my_guests[4]}, {my_guests[5]}. Sorry, we will have only 2 guests")

guest_delete_operation1 = my_guests.pop(0)
print(f"Hi, {guest_delete_operation1}. Sorry, we have to shrink our team. We will boring.")
print(my_guests)

guest_delete_operation2 = my_guests.pop(0)
print(f"Hi, {guest_delete_operation2}. Sorry, we have to shrink our team. We will boring.")
print(my_guests)

guest_delete_operation3 = my_guests.pop(0)
print(f"Hi, {guest_delete_operation3}. Sorry, we have to shrink our team. We will boring.")
print(my_guests)

guest_delete_operation4 = my_guests.pop(0)
print(f"Hi, {guest_delete_operation4}. Sorry, we have to shrink our team. We will boring.")
print(my_guests)


print(f"{my_guests[0]}, our welcome ticket for you is still.")
print(f"{my_guests[1]}, our welcome ticket for you is still.")

del my_guests[0]

print(my_guests)

del my_guests[0]

print(my_guests)

# Ex 3.8
# travelling DZ
my_countries = ['Ukraine', 'Poland', 'Belarus', 'England', 'USA']
print(my_countries)

sort_list1 = sorted(my_countries)
print("It is the alphabetic sorted list:")
print(sort_list1)
print("\n")

print("It is the original list:")
print(my_countries)
print("\n")

print("It is the reverse sorted list with 'sorted' function:")
sort_list2 = sorted(my_countries, reverse=True)
print(sort_list2)
print("\n")

print("It is the original list:")
print(my_countries)

my_countries.reverse()
print(f"There are my countries already save reverse function: \n {my_countries}")

my_countries.sort()
print(f"There are my countries sorted already save reverse and sort functions: \n {my_countries}")

my_countries.sort(reverse=True)
print(f"There are my countries sorted already with parameter reverse=true in sort function: \n {my_countries}")

# Ex 3.9
my_guests_new = ['Vika', 'Sveta', 'Kirill', 'Marsik']
print(f"Count of my guests are: {len(my_guests_new)}")

# Ex 3.10
my_dev_skills = ['Python', 'JavaScript', 'HTML', 'CSS', 'PHP', 'MySQL', 'Git']
print(f"Original list is: \n {my_dev_skills}\n")

sorted_alphabet_skills = sorted(my_dev_skills)
print(f"Sorted list as alphabet in copy is: \n {sorted_alphabet_skills}\n")

sorted_alphabet_skills_reversed = sorted(my_dev_skills, reverse=True)
print(f"Sorted list as reversed alphabet in copy is: \n {sorted_alphabet_skills_reversed}\n")

my_dev_skills.reverse()
print(f"Original list as reversed in local is: \n {my_dev_skills}\n")

my_dev_skills.sort()
print(f"Original list as alphabet and reversed in local is: \n {my_dev_skills}\n")

my_dev_skills.sort(reverse=True)
print(f"Original list as alphabet and reversed with parameter reverse=True with function sort in local is: \n {my_dev_skills}\n")