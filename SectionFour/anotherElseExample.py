avaliable_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in avaliable_exits:
    chosen_exit = input("please choose a direction:")
    if chosen_exit.casefold() == "quit":
        print("game over")
        break

else:
    print("arent you glad you got out of there ")
