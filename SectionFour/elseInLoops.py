numbers = [1, 45, 32, 12, 60]

# will output print statement because 8 is divisible by 32
# when our loop finds a value thats not acceptable, our code breaks out of the loop
# this means the loop will only terminate normally if all the values are acceptable
for number in numbers:
    if number % 8 == 0:
        # reject list
        print("these numbers are unacceptable")
        break
else:
    print("all those numbers are fine")

# if you change 32 to 31, nothing will print
