def is_palindrome(string):
    backwards = string[::-1]
    return backwards == string == string.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


word = input("please enter a word to check")
if palindrome_sentence(word):
    print("{} is a palindrome".format(word))
else:
    print("{} is not a palindrome".format(word))
