answer = 5

print("please guess a number between 1 and 10: ")

# expects an integer in the input
guess = int(input())

if guess < answer:
    print("please guess higher")
    guess = int(input())
    if guess == answer:
        print("well done, you guessed it")
    else:
        print("sorry not guess correctly")
elif guess > answer:
    print("please guess lower")
    guess = int(input())
    if guess == answer:
        print("well done, you guess it")
    else:
        print("you have not guess correctly")
else:
    print("you got it the first time")
