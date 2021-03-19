# removing rogue values from an unsorted list can bedone with less code that previous examples
# when removing an item from a list while iterating forward, the size of the list changes
# things go wrong here because items that are removed, shuffle down to fill in the gap
# that messes up the index number as we work fowards
# so we can solve this problem by iterating backwards. this allows the size of the swquence to be changed
# without causing any problems


data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

# this code will remove the correct values regardless of order
for index in range(len(data) - 1, -1, -1):
    if data[index] < min_valid or data[index] > max_valid:
        print(index, data)
        del data[index]
print(data)
