# create a list of unconfirmed users, and other empty list about confirm users
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# check of every user, when the unconfirmed users wil be in the array.
# Every user which was checked, - after checking will transfer to list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# show of all confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
