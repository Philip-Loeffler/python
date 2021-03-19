empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]



# create a list by concating list
numbers = even + odd
print(numbers)

# creates a list of all numbers but sorted
sorted_numbers = sorted(numbers)
print(sorted_numbers)


# will print out a list of strings
digits = sorted("432985617")
print(digits)

# will return a list but items will be in the same order
digits = list("432985617")

# one way to copy a list
more_numbers = list(numbers)
print(more_numbers)

# will show false, because they are not the same list, but they contain the same items in the same order
print(numbers is more_numbers)

# copy a list but with a slice by slicing an existing list
more_numbers = numbers[:]

# best way to copy list is to use the copy method
more_numbers = numbers.copy()
