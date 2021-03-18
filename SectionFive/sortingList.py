
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# extend will combine and add all of the iterables from the list and adds them to it
even.extend(odd)
print(even)

# sort will sort the sequence of numbers
# sort method doesnt create a copy of the list, it rearranges the items of the list
# lists are mutable and their contents can be changed
even.sort()
print(even)
another_even = even

# same list printed out twice,
print(another_even)

# will sort in the reverse order
even.sort(reverse=True)
print(even)

# this list will be reversed because of mutability
print(another_even)
