
# value error = raised when an operation or function receives an arguemnt that has the right type
# but an inappropriate value, and the situation is not described by a more precise exception
def banner_text(text):
    screen_width = 50
    if len(text) > screen_width - 4:
        raise ValueError("string {0} is larger then specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centered = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered)
        print(output_string)


banner_text("always look on the bright side of life")


# def banner_text(text, screen_width):

#     if len(text) > screen_width - 4:
#         raise ValueError("string {0} is larger then specified width {1}"
#                          .format(text, screen_width))

#     if text == "*":
#         print("*" * screen_width)
#     else:
#         centered = text.center(screen_width - 4)
#         output_string = "**{0}**".format(centered)
#         print(output_string)
