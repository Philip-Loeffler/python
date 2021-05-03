# unordered, and doesnt contain duplicates.
# items are not accessed via key
# most be immutable objects
# used less than other data structures


farm_animals = {"sheep", "cow", "hen"}

for animal in farm_animals:
    print(animal)

# the built in function for sets
wild_animals = set(["Lion", "tiger", "panther", "elephant", "hare"])


for animal in wild_animals:
    print(animal)


# adding new memeber to a set
# also there is no order with sets, by nature they are unordered
farm_animals.add("horse")
wild_animals.add("horse")

print(farm_animals)
print(wild_animals)


empty_set = set()
empty_set.add("a")

# the add method will fail. reason is because = {} is creating a dict, and dicts dont have an add method
# empty_set_2 = {}
# empty_set_2.add("a")


even = set(range(0, 40, 2))
print(even)

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)

# unions

even_2 = set(range(0, 40, 2))
print(even_2)
print(len(even_2))

squares_tuple_2 = (4, 6, 9, 16, 25)
squares_2 = set(squares_tuple_2)
print(len(squares_2))

print(even_2.union(squares_2))
print(squares.union(even_2))

print(even_2.intersection(squares_2))


print(sorted(even))
squares = set(squares_tuple)
print(sorted(squares))
# can use the difference method to subtract. using the difference method is only applicable to sets
print(sorted(even.difference(squares)))
print(sorted(even - squares))
