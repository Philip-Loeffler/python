answer = 5

print("please guess a number between 1 and 10: ")

# expects an integer in the input
guess = int(input())

if guess != answer:
    if guess < answer:
        print("please guess higher")
    else:  # guess must be greater than answer
        print("please guess lower")
    guess = int(input())
    if guess == answer:
        print("well done, you've guess it")
    else:
        print("sorry you have not guess correctly")
else:
    print("you got it first time")


# if guess == answer:
#     print("you got it first time")
# else:
#      if guess < answer:
#         print("please guess higher")
#     else:  # guess must be greater than answer
#         print("please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("well done, you've guess it")
#     else:
#         print("sorry you have not guess correctly")

