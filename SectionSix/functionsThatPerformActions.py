
# not all functions return a value
# some functions return something back to the calling code


# when you define a function to have positional arguments, the arugments are assigned to the parameter in
# their corresponding position.
# if you want a function to return a value, use the return keyword to specify the value that should be returned
# not all functions return something sueful, some functions perform an action, rahter than producing a value
# if you dont explicity return a value, python will automatically return none
# it is valid to explicity return none from your functions. you might do that to indicate something wanst found
# for example the dictionary method get does this
def banner_text(text):
    screen_width = 80
    if len(text) > screen_width - 4:
        print("eek")
        print("the text is to long to fit in the specifed width")

    if text == "*":
        print("*" * screen_width)
    else:
        centered = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered)
        print(output_string)


banner_text("always look on the bright side of life")
