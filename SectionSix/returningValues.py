import random


def get_integer(prompt):
    # keep on looping until the input is valid
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            # the return statement causes the execution to leave the function, and return to the next statement in the code
            # if its true that is
            return int(temp)
    #    else: dont need the else, because if a valid number is entered the function will return. if it is not a valid number it goes below the return
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
