# sorting function can be used to sort any iterable object

pangram = "the quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
# sorted function will take any iterable, and return it as a list
# upper case letters will be sorted first too

print(letters)


numbers = [2.3, 4.5, 8.7, 9.2, 1.6]
sorted_numbers = sorted(numbers)
# we get a DIFFERENT list back.
print(sorted_numbers)


# difference between the two is you have to assign the sorted to a new return variable,
# sort you do not
numbers.sort()
print(numbers)

# will print out none because sort doesnt return anything
# so this wont work ya jabroni
another_sorted_numbers = numbers.sort()
print(another_sorted_numbers)

# passing a string literal
missing_letter = sorted("the quick brown fox jumped over the lazy dog")
print(missing_letter)
