age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# -------------------

apple_count = 15
if apple_count < 5:
    piece_cost = 30
elif apple_count < 10:
    piece_cost = 20
elif apple_count < 100:
    piece_cost = 10
else:
    piece_cost = 7

print(f"Your cost for to buy fruit for 1 piece is ${piece_cost}.")
