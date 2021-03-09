for i in range(1, 13):
    for j in range(1, 13):
        print("{0} times {1} is {2}".format(j, i, i * j))
    print("--------------")

# first loop runs 1 time, then inner loop will run all the way through
# then come back to the outer loop, which then again but incremented one time
# and inner loops runs through fully
