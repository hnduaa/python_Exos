def filter_even(numbers):
    return list(filter(lambda x : (x%2 == 0)))
# Test case
print(filter_even([1, 2, 3, 4, 5, 6])) 