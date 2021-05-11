def center_text2(*args, sep=' ', end_char='\n', centered_file=None, flush_me=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end_char,
          file=centered_file, flush=flush_me)


# this will write your code to a new file named centered
with open("centered", mode="w") as centred_file:

    center_text2("first", "second", 3, 4, "spam",
                 sep=":", centered_file=centred_file)


def center_text3(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    # this is indicating that a string should be returned, when the function is called
    return " " * left_margin + text


print(center_text3("spam and eggs"))
print(center_text3("spam and eggs", 1, 2, 3, sep=":"))
# same concept as the center_text3 method
print("=" + str(12 * 3))
# assigning the return value from our function to a variable named s1, then printing it
s1 = center_text3(12, "spam", "spam")
print(s1)
