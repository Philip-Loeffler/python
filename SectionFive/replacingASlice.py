computer_parts = ["computer", "monitor",
                  "keyboard", "mouse", "mouse mat"]

print(computer_parts)

# replacing third index with trackball
computer_parts[3] = "trackball"
print(computer_parts)

# replacing both items at once with a slice

print(computer_parts[3:])

# by doing this, you will get each character of the trackball added individually, so it will look like:
# [computer, monitor, keyboard, t, r, a, c, k, b, a, l, l]
computer_parts[3:] = "trackball"
print(computer_parts)

# by doing this you will have trackball be added to the list without each string seperated
computer_parts[3:] = ["trackball"]
print(computer_parts)
