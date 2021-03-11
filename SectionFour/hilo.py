low = 1
high = 1000


print("please think of a number between {} and {}".format(low, high))
input("press enter to start")

guesses = 1


while True:
    # calculates midpoint to know what to guess next
    guesses = low + (high - low) // 2
    high_low = input(
        "my guess is {}. should I guess higher or lower? enter "
        "h or l, or c if my guess was correct".format(guesses)).casefold()
    if high_low == "h":
        # guess higher. the low end of the range becomes greater than the guess
    elif high_low == "l":
        # guess lower. the high end of the range becomes one less than the guess
    elif high_low == "c":
        print("I got it in {} guesses".format(guesses))
    else:
        print("please enter h, l, or c")
