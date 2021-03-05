day = "Monday"
temperature = 30
raining = True

if day == "Saturday" and temperature > 27 and not raining:
    print("go swiming")
else:
    print("leanr python")


# truthy values
# 0 is evaluated to false when its in a boolean expression
if 0:
    print("true")
else:
    print("false")


name = input("please enter your name: ")
if name:
    print("hello, {}".format(name))
else:
    print("are you the man with no name?")

# if you put in an input it will evaluate to true
# if you put in an empty string, it will evaluate to false


# should do it like this

name = input("please enter your name: ")
if name != "":
    print("hello, {}".format(name))
else:
    print("are you the man with no name?")
