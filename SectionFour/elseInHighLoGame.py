low = 1
high = 1000


print("please think of a number between {} and {}".format(low, high))
input("press enter to start")

guesses = 1

# will loop until as long as low doesnt equal high, when they are equal the loop will terminate
while low != high:
    # calculates midpoint to know what to guess next
    guesses = low + (high - low) // 2
    high_low = input(
        "my guess is {}. should I guess higher or lower? enter "
        "h or l, or c if my guess was correct".format(guesses)).casefold()
    if high_low == "h":
        low = guesses + 1
    elif high_low == "l":
        high = guesses - 1
    elif high_low == "c":
        print("I got it in {} guesses".format(guesses))
        break
    else:
        print("please enter h, l, or c")

    guesses = guesses + 1
else:
    print("you thought of the number {}".format(low))
    print("i got it in {} guess".format(guesses))
