data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200


# reversed lets us use enemurate
# when using reversed, the index positions relate to the data in reversed order
# so in this case, the 0 index will have 108 on it. index will still start at 0
for index, value in enumerate(reversed(data)):
    print(index, value)


# doing this, we will see all of the values with there correct index positons
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    print(index, value)
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]
