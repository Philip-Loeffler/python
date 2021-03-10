avaliable_exits = ["north", "south", "east", "west"]

# casefold is letting the string comparison work regardless of capital letters
chosen_exit = ""
while chosen_exit not in avaliable_exits:
    chosen_exit = input("please choose a direction:")
    if chosen_exit.casefold() == "quit":
        print("game over")
        break

print("arent you glad you got out of there ")


# challenge 10
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

# challenge 11 with continue
for i in range(21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)

# without continue
for i in range(21):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
