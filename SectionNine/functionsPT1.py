def python_food():
    width = 80
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2
    print("" * left_margin, text)


def center_text(text):
    # this is just coverting the argument to a string, want to do this so you can pass in numbers
    # because passing in a number without this would fail because of the len
    text = str(text)
    left_margin = (80 - len(text)) // 2
    print("" * left_margin, text)


# call function
python_food()
# showing difference in paramters entered
center_text("spam, and eggs")
center_text("spam, spam, and eggs")
center_text("spam, spam, spam, and eggs")

# seeing *args means you can pass any amount of variables that you want, seperated by comma's
# the print method has args in its definition, that is why we are able to provide it the arguments
# in the line below
print("first", "second", 3, 4, "spam")
