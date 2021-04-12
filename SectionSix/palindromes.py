def is_palindrome(string):
    backwards = string[::-1]
    return backwards == string == string.casefold()
# this will make the strings not case sensitive

# could also be written like


def is_palindrome2(string):
    return string[::-1] == string == string.casefold()


word = input("please enter a word to check")
if is_palindrome(word):
    print("{} is a palindrome".format(word))
else:
    print("{} is not a palindrome".format(word))
