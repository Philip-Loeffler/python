shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    print("buy " + item)

# will print out list without spam in it
for item in shopping_list:
    if item != "spam":
        print("buy " + item)

for item in shopping_list:
    if item == "spam":
        continue

    print("buy " + item)

# when you come to spam in the for loop, the if blocks see's it, then goes to continue. once you get to continue
# all the code underneath it isnt executed, so spam wont be printed, it then goes back up to top of for loop
