# range creates a sequence of numbers, an increments by one, and stops at the defult number
for i in range(1, 13):
    print("no {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("*" * 80)
# both of the prints are in the same block
# when this prints it looks like "no 2, squared is 4, and cubed is eight"
for i in range(1, 13):
    print("no {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
print("*" * 80)
# here they are not in the same block of code
