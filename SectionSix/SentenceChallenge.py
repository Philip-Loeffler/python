def palindrome_sentence(sentence):
    string = ""
    # this will produce a string that will only use letters and digits
    for char in sentence:
        if char.isalnum():
            string += char
    return string[::-1] == string == string.casefold()


# shit i totally spaced on thinking you needed to have sentence in your return here sheesh
