def bin_search_mock(list_, target_value):
   for index in range(len(list_)):
        if list_[index] == target_value:
            return index
   return -1

# List_ is the sorted list of different integers.
# Returns the index of target_value.
# If not found, returns -1
def bin_search(list_, target_value):
    return bin_search_mock(list_, target_value)

def Assert(expected, actual):
    if expected == actual:
        print("OK")
    else:
        print(f"Test not ok:\nExpected: {expected}\nActual: {actual}\n")

test_list = [1, 2, 4, 5, 6, 8, 9]

Assert(0, bin_search(test_list, 1))
Assert(2, bin_search(test_list, 4))
Assert(6, bin_search(test_list, 9))
Assert(-1, bin_search(test_list, 3))
Assert(-1, bin_search(test_list, -3))
Assert(-1, bin_search(test_list, 13))
