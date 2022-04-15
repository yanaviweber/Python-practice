alien_0_my_dictionary = {'color': 'blue', 'speed': 'slow'}
# print(alien_0_my_dictionary['points']) ---- print "Error message of 'point' "

# point_value = alien_0_my_dictionary.get('points') --- print "None"
point_value = alien_0_my_dictionary.get('points', 'No point value assigned.')
print(point_value)
