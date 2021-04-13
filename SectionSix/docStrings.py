import random


def get_integer(prompt):
    # Get an integer from Standard input
    # the function will continue looping, and prompting the user, until a valid int is entered
    # param prompt: the string that the user will see, when they're prompted to enter a value
    # return: the integer that the user enters
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("{0}. is not a valid number".format(temp))


highest = 1000
answer = random.randint(1, highest)
guess = 0
print("please guess a number between 1 and {}: ".format(highest))


while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("well done, you guess it")
        break
    else:
        if guess < answer:
            print("please guess higher")
        else:
            print("please guess lower")
