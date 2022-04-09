list = [7, 50, 98, 456, 1]

for l in list:
    if (l == 50):
        print("found: ", l)

for i in range(len(list)):
    if list[i] == 50:
        print("found 50 at position: ", i)

list = [1, 2, 4, 5, 1, 6, 1, 1, 8, 4, 5, 7]

sum = 0
for item in list:
    sum += item

print(sum)

res = 1
for item in list:
    res *= item

print(res)

count = 0
for item in list:
    if item > 3:
        count += 1

print(count)

list3 = []
for item in list:
    if item > 3:
        list3.append(item)

print(list3)
print(list3[(len(list3)-1)//2], list3[(len(list3)-1)//2+1])
print(list3[len(list3)-2])

# Ex: search all items which greater then previous one
count = 0
test_array = [2, 9, 1, 0, 69, 4, 7, 56, 82, 47]
for idx in range(1, len(test_array)):
    if test_array[idx] > test_array[idx-1]:
        count += 1
print(count)
print("\n")
# Ex: count numbers divisible by three
count = 0
example_array = [6, 96, 44, 2, 7, 0, 36, 24, 45, 90]
for index in range(1, len(example_array)):
    if example_array[index] > example_array[index-1] and example_array[index] % 3 == 0:
        count += 1
        print(example_array[index], end=" ")

print(f"\nThere are number of elements: {count} \n")

# Ex: count number of even numbers in the list

count = 0
for item in example_array:
    if item % 2 == 0:
        count += 1
        print(item, end=" ")
print(f"\nThere are number of even elements: {count} \n")


