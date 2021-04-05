name = "tim"
age = 10


print(name, age, "python", 2020)

# each value is seperated with a comma and a space
print(name, age, "python", 2020, sep=", ")

# end will tell print to print a space after printing, instead of a new line
for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=" ")
        print()
