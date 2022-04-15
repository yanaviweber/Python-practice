squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

squares_test = []
for value in range(1, 20):
    squares_test.append(value**2)
print(squares_test)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1, 11)]
print(squares)

for value in range(1, 11):
    print(value**2, end=" ")


