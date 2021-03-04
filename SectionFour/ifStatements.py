name = input("please enter your name")
# the {} are indictating where the string value from format is suppose to go
# putting int in front of input lets input know it is expecting an integer, not a string
age = int(input("how old are you? {0}".format(name)))
print(age)

if age >= 18:
    print("ehhh old enough to vote")
    # just showing code executing in different blocks
    print("please put an x in the box")
else:
    print("please come back in {0} years".format(18 - age))


# just another way to do the same thing
if age < 18:
    print("please come back in {0} years".format(18 - age))
else:
    print("ehhh old enough to vote")
    print("please put an x in the box")
