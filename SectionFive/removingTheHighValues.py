data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]


min_valid = 100
max_valid = 200


stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)
del data[:stop]
print(data)


# process high values in the list
start = 0
# we want to work backwards so we start at the index one less of the length of the list
# this will get 15 to 0. the early code got rid of the first two items
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        # we have the index of the last item to keep.
        # set "start" to the positon of the first
        # item to delte, which is 1 after "index"
        start = index + 1
        break
    print(index)
del data[start:]
