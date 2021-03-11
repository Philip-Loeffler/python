import random

# randint function creates a random number within the range of numbers we pass it
highest = 10
answer = random.randint(1, highest)

print("please guess a number between 1 and {}: ".format(highest))
guess = int(input())


if guess == answer:
    print("you got it the first time")
else:
    if guess < answer:
        print("please guess higher")
    else:
        print("please guess lower")
    guess = int(input())
    if guess == answer:
        print("well done, you've guessed it")
    else:
        print("sorry, you have not guess correctly")


# with while

while guess != answer:
    guess = int(input())

    if guess == answer:
        print("well done, you guess it")
        break
    else:
        if guess < answer:
            print("please guess higher")
        else:
            print("please guess lower")
