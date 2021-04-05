menu = [
    ["eggs", "bacon"],
    ["eggs", "sausage", "bacon"],
    ["eggs", "spam"],
    ["eggs, sausage", "spam", "bacon", "spam", "tomato", "spam"],
]

# write code to print out all the meals in the menu, bnut with spam removed


# this will only remove the first occurence
if "spam" in menu:
    menu.remove("spam")
    print(menu)

# this will remove all occurences
while "spam" in menu:
    menu.remove("spam")
    print(menu)


for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]

    print(meal)

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item)
        print()
