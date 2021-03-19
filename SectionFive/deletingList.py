data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

# this will delete the first two entries in our list. so 4, 5
del data[0:2]
print(data)

del data[14:]
print(data)

min_valid = 100
max_valid = 200

# this wont return the correct data
# the reason is because we are changing the size of the object
# after the first loop deletes the 4 at position 0
# the second loop see's 5 at position 0
# which will be returned, even though the min_valid is set to 100
for index, value in enumerate(data):
    if (value < min_valid) or (value > max_valid):
        del data[index]

print(data)
