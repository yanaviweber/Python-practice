motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('myDucati')
print(motorcycles)

motorcycles_park_test = []
motorcycles_park_test.append('honda')
motorcycles_park_test.append('yamaha')
motorcycles_park_test.append('suzuki')
print(motorcycles_park_test)

motorcycles_park_test.insert(0, 'ducati')
print(motorcycles_park_test)
del motorcycles_park_test[0]
print(motorcycles_park_test)
del motorcycles_park_test[1]
print(motorcycles_park_test)

poped_motorcycle = motorcycles_park_test.pop()
print(motorcycles_park_test)
print(poped_motorcycle)

third_motorcycle_test_park = ['honda', 'yamaha', 'suzuki']
last_owned = third_motorcycle_test_park.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
second_owned = third_motorcycle_test_park.pop(0)
print(f"The second motorcycle I owned was a {second_owned.title()}.")

fourth_motorcycle_test_park = ['honda', 'yamaha', 'suzuki', 'ducati']
print(fourth_motorcycle_test_park)
fourth_motorcycle_test_park.remove('ducati')
print(fourth_motorcycle_test_park)


fifth_motorcycle_test_park = ['honda', 'yamaha', 'suzuki', 'ducati']
print(fifth_motorcycle_test_park)
too_expensive = 'ducati'
fifth_motorcycle_test_park.remove(too_expensive)
print(fifth_motorcycle_test_park)
print(f"\nA {too_expensive.title()} is too expensive for me")

print(motorcycles[3])
print(motorcycles[-1])

