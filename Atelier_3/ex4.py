strings = ["apple", "banana", "cherry", "kiwi", "pear"]
def filter_by_length(strings, number):
    return list(filter(lambda x : len(x)<=5,strings))

print(filter_by_length(strings, 5)) # Output: ['apple', 'kiwi', 'pear']