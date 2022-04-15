alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])


new_points = alien_0['points']
print(f"You just earned {new_points} points!")

print("\n------------------------")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print("\n--------- Empty dictionary with input elements in the empty dictionary ---------------")

alien_0_Second = {}
alien_0_Second['color'] = 'purple'
alien_0_Second['points'] = 8
print(alien_0_Second)
print("\n--------- The dictionary with change elements in the dictionary ---------------")
alien_0_Third = {'color': 'green'}
print(f"The alien is {alien_0_Third['color']}.")

alien_0_Third['color'] = 'yellow'
print(f"The alien is now {alien_0_Third['color']}.")

print("\n--------- The dictionary with change elements in the dictionary with if-elif-else ---------------")
alien_0_moving = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0_moving['x_position']}.")

# alien_0_moving['speed'] = 'fast' ----- example if I want Alien will be moving fast ----------

# Alien is moving in the right.
# Calculate moving value by basics current speed.
if alien_0_moving['speed'] == 'slow':
    x_increment = 1
elif alien_0_moving['speed'] == 'medium':
    x_increment = 2
else:
    # Alien speed is fast.
    x_increment = 3
# New point position of alien is sum of the old point position plus growing speed value.
alien_0_moving['x_position'] = alien_0_moving['x_position'] + x_increment

print(f"New position: {alien_0_moving['x_position']}.")

print("\nDelete \"Key -> value\" in the dictionary with operation \"del\"")
alien_0_for_deleting_example = {'color': 'green', 'points': 5}
print(alien_0_for_deleting_example)

del alien_0_for_deleting_example['points']
print(alien_0_for_deleting_example)

print("\nThe dictionary with objects of one same type of objects.")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")


