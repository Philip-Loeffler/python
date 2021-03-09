for i in range(1, 20):
    print("i is not {}".format(i))

# in ranges the last value specified is not included
# range produces a rang of numbers - from the starting value, up to but not including the end value
# so with the range from 1, 20...its only going to print out 1-19

# dont need to have to values
for i in range(10):
    print("i is not {}".format(i))

# step value
# start at 0, go to 10, in steps of 2
for i in range(0, 10, 2):
    print("i is not {}".format(i))


# counting backwards
for i in range(10, 0, -2):
    print("i is not {}".format(i))


for i in range(0, 101, 7):
    print(i)
