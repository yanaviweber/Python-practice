# Ex 7.1

choose_car = input("What car do you want to rent? ")
print(f"Let me see I can find you a {choose_car}.")

print("\n---------------------------")
# Ex 7.2
count_invite_quests = input("How many quests will you invite on your place? ")
count_invite_quests = int(count_invite_quests)

if count_invite_quests > 8:
    print("You are have to waiting..")
else:
    print("Your place is ready now. Welcome!")

print("\n---------------------------")
# Ex 7.3
your_number = input("Please, enter your number: ")
your_number = int(your_number)

if your_number % 10:
    print("This number is not 0 from % 10.")
else:
    print("This number is ok.")