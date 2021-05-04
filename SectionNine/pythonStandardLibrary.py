import shelve
import random
# this is showing us all of the built in methods for us to use
print(dir())
print(dir(__builtins__))
for m in dir(__builtins__):
    print(m)

# all of the objects available to us in the shelf module
print(dir())
print()
print(dir(shelve))

# returning all without the underscore
for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print(obj)

# will give detailed information on how to use shelve
help(shelve)

# to get help on individual functions
help(random.randint)
