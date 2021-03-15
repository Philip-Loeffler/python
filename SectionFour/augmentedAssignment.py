x = 23

# 24
x += 1
print(x)

# 20
x -= 4
print(x)

# 100
x *= 5
print(x)

# 25
x //= 4
print(x)

# 5.0 - note conversion from into float
x /= 5
print(x)


# 25.0 - x still represents a float
x ** 2
print(x)

# 0.0 -= 25 is exactly divisble by 5
x %= 5
print(x)


# this is augmented assignenment. Here is why its better
# with this way guesses = guesses + 1 python is creating a new variable
# it binds the new variable to the result of the peroming the calulation then destroys the original variable
# using an augment assignemnt, it can perform the operatin in-place where possibly, modifying the original variable
# guesses += 1


greeting = "good "

greeting += "moring"
printing(greeting)

greeting *= 5
print(greeting)
