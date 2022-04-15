alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


# create an empty list of aliens
my_aliens = []

# create 30 new aliens through range() function
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    my_aliens.append(new_alien)

# change parameters ony for first 3 aliens
for alien in my_aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


# show the first 5 aliens with "for" cycle
for alien in my_aliens[:5]:
    print(alien)
print("...")

# show all aliens through "print"
print(f"Total number of aliens: {len(my_aliens)}")

