# sometimes we need to keep looping as long as a condition is true, ands stop when it becomes false
# while loops are best used for this

# the basic form looks like so
# while <condition>
# execute block of code
# as long as condition in loop is true it will continue, if it is false it exits


# for i in range(10):
#     print("i is now {}".format(i))
# demonstrate same code with while loop


i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1

avaliable_exits = ["north", "south", "east", "west"]

# we initalize an empty string
# so the program see's that the empty string is not in the list, making it true, thus entering the loop
chosen_exit = ""
while chosen_exit not in avaliable_exits:
    chosen_exit = input("please choose a direction:")

print("arent you glad you got out of there ")


# one of the important features of while loops is that they can be used to determine in advance how
#  many times  you will need to loop
#  a for loop will repeat for each item in a pre-detemrined sequence, whereas with a while loop
# you dont need to know how many timers the loop will execute
