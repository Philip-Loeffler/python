# args allows for multiple params
# you loop over args, so the text variable is going to hold all of the arguments
def center_text(*args):
    text = ""
    for arg in args:
        text += str(arg) + " "
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)

# different signatures
# which means a way of referring to a set of parameters in a function definitions
# because the print function has the end, file, flush params, we can pass those into our function as well,
# so that when we call center_text2, we have the opportunity to pass end_char to the end param in print ect ect


def center_text2(*args, sep=' ', end_char='\n', centered_file=None, flush_me=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end_char,
          file=centered_file, flush=flush_me)


center_text("first", "second", 3, 4, "spam")
print()
center_text2("first", "second", 3, 4, "spam", sep=":")
