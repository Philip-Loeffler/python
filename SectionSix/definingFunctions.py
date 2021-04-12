


def multiply():
    result = 10.5 * 4
    return result

# because our function is returning a value, we can find out function to answer, and print out that answer
answer = multiply()
print(answer)

# parameters are like placeholders for the real values that you'll pass to your function
# they are just variables, but they are given a value, when you call the function.
def multiply2(x, y):
    result = x * y
    return result

# arguments are the values that will be used by formal parameters, when we call a function
# each parameter must be give a value, by providing an arugment in the function call
# providing values is passing the arguements
answer2 = multiply2(10.5, 4)
print(answer2)


forty_two = multiply2(6,7)
print(forty_two)

# function call is another type of expression

for val in range(1, 5):
    two_times = multiply2(2, val)
    print(val)