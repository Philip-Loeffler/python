age = 24
# string function makes an int into a string
print("my age is " + str(age) + " years")

# python 3.6 made this easier with the format function
print("my age is {0} years".format(age))

# these are replaced with the values in the parenthese after/fromat, the firsat value goes into {0}, and so on
print("there are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}".format(
    31, "jan", "march", "may", "jul", "august", "oct", "dec"))

# 0 index is populated with 30, the 1 is populated with 31 and so on
print("jan: {2}, feb: {2}, march: {1}, april:{0}, jun:{1}".format(30, 31, 222))
