numbers = (0, 1, 2, 3, 4, 5)

print(numbers, sep=";")
# unpacked, so the print statement will look like this 0 1 2 3 4 5
print(*numbers, sep=";")

# using *args, we can provide a variable number of arguments to our function
# using star args means that it reprersents an unpacked tuple in this case


def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)


print()
# using args allows us to write functions that contain 0 or more arguments
test_star()
