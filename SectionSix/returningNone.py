def multiply(x, y):
    result = x * y
    return result


def return_none(x, y):
    result = x * y
    # return result


def is_palindrome(string):
    backwards = string[::-1]
    return backwards == string == string.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


# word = input("please enter a word to check")
# if palindrome_sentence(word):
#     print("{} is a palindrome".format(word))
# else:
#     print("{} is not a palindrome".format(word))


answer = multiply(18, 3)
print(answer)

# if you look at function up top, you will see that no return is there
none = return_none(20, 20)
print(none)

# not all functions return a value
# some functions return something back ot the calling code
# one example is the sort method that is used to sort a list
# the sort function didnt return anything useful, but it did perofrm  a useful function, that is..sorting the list
