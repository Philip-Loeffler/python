# options = ["0", "1", "2", "3", "4"]

# # casefold is letting the string comparison work regardless of capital letters
# chosen_option = ""
# while chosen_option not in options:
#     chosen_option = input("please choose an option:")
#     if chosen_option == "0":
#         print("exit")
#         break


# print("arent you glad you got out of there ")


# write a program to print a number of options, and allow the user to select an option from the list
# the options should be numbered 1-9
# make sure there is at least 4


print("please choose your option from the list below:")
print("1:\tLearn Python")
print("2:\tLearn Java")
print("3:\tLearn swimming")
print("4:\tLearn have dinner")
print("5:\tLearn go to bed")
print("0:\tLearn exit")


while True:
    choice = input()

    if choice == "0":
        break
    elif choice in "12345":
        print("you chose {}".format(choice))
    else:
        print("please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tLearn swimming")
        print("4:\tLearn have dinner")
        print("5:\tLearn go to bed")
        print("0:\tLearn exit")
