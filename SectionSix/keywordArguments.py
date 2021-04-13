def banner_text(text=" ", screen_width=80):

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
banner_text("if life seems jolly rotten")
banner_text()
banner_text(screen_width=60)
