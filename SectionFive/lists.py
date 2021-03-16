# sequence - an ordered collection of item. order is important because we need to be able to grab their index
# anything you can iterate over is an iterable
# all sequences types can be iterated over


computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]


for part in computer_parts:
    print(part)

print()
print(computer_parts[2])

print(computer_parts[0:3])
print(computer_parts[-1])


# strings are immutable, which means they cannot be changed
# lists on the other hand are mutable, you can change the contents of a list
