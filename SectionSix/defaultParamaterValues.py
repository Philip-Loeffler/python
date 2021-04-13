# if a function defines two positional parameters then you must provide two arguments when calling it
# UNLESS the parameter have default values, that is. If you provide a default valuie for a parameter,
# then its not necessary to provide a coresponding arugment for it

# having the equals 80 in the parameters is giving the function a default value
def banner_text(text, screen_width=80):

    if len(text) > screen_width - 4:
        raise ValueError("string {0} is larger then specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centered = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered)
        print(output_string)


banner_text("always look on the bright side of life", 60)
# by not adding in the extra parameter here, it will default to 80
banner_text("if life seems jolly rotten")
