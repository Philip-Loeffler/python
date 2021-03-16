# strings are immutable, which means they cannot be changed
# the following are immutable in python - int, float, bool, str, tuple, frozenset, byte

# id returns the identity of an object. it must be guaranteed to be unique and constant
# for this object during its lifetime
# both print statements will have same id
result = True
another_result = result
print(id(result))
print(id(another_result))

# false print statement id is different
# were not able to change the result of true, but bound a false to a new value ie result
result = False
print(id(result))


# new example

result = "correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))
