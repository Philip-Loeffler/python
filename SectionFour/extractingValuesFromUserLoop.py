number = input(
    "please enter a serious of number, using any separators that you like: ")
seperators = ""


for char in number:
    if not char.isnumeric():
        seperators = seperators + char

print(seperators)


# sum is adding up all of the numbers for us
values = "".join(
    char if char not in seperators else " " for char in number).split()
print(sum([int(val) for val in values]))
