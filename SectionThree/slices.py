parrot = "Norwegian Blue"

# start at position 0 and slice up to, but not including position six = Norweg
print(parrot[0:6])

print(parrot[3:5])  # We
print(parrot[0:9])  # Norwegian
# blue. Remember, it will print up to but not include, so thats why blue is here
print(parrot[10:14])


# negative numbers
# negative numbers just count from the end of the string
print(parrot[-4:2])  # cant go backwards from starting position
print(parrot[-4: -2])  # BL

#steps in slices
# nre   starts at index 0, extracts all characters up to but not including index six, and in steps of 2
print(parrot[0:6:2])

# slicing backwards
letters = "abcedfghijklmnopqrstuvwxyz"
backwards = letters[25:: -1]
print(backwards)

p = letters[15]
hi = letters[7: -17]
l = letters[11]
i = letters[8]

print(p + hi + l + i + p)

