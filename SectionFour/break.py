shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    if item == "spam":
        break

    print("buy " + item)

# loop terminates when it gets to break. so the output is going to by mik, pasta, eggs


item_to_find = "spam"
found_at = None

# len() is a built in function to check for length. similar to .length
# for index in range(6)
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

print("item found at position {}".format(found_at))


# adding in the break will terminate the program once line 19 is true. so it wont continue to loop over.
