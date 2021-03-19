data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]


min_valid = 100
max_valid = 200


# this code will only work when the data is sorted

# 1. process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)
# remember that when we delete from a slice it is up to but not including: [0: 4, 1: 5, 2: 104] - doesnt delete 104
del data[:stop]
print(data)
