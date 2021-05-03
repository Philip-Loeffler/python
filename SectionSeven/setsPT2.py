even = set(range(0, 40, 2))
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares))

print(sorted(even))
print(squares)
even.difference_update(squares)
print(sorted(even))


# symetric difference of 2 sets.
# all members that are in one set or the other, but not both

print("symmetrical even minus squares")
print(sorted(even.symmetric_difference(squares)))
print("symmetrical squares minus even")
print(sorted(squares.symmetric_difference(even)))


squares.discard(4)
squares.remove(16)
# eight isnt in the set, so should do nothing
squares.discard(8)

# trapping error and processing a message
try:
    squares.remove(8)
except KeyError:
    print("the item 8 is not a member of the set")


if squares.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares):
    print("even is a superset of squares")

# frozen set
# immutable, once created, cant modify it
even = frozenset(range(0, 100, 2))
print(even)
