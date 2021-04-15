# the ole fizzbuzz


def fizz_buzz(x):
    if x % 3 == 0:
        return "fizz"
    elif x % 5 == 0:
        return "buzz"
    elif x % 5 == 0 and x % 3 == 0:
        return "fizzbuzz"


for i in range(1, 101):
    print(fizz_buzz(i))
