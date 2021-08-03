# Write a function that stutters a word as if someone is struggling to read it. The first two
# letters are repeated twice with an ellipsis ... and space after each, and then the word is
# pronounced with a question mark ?.

def stutter(word):
    x = 2*(word[:2] + "...")
    return(x + word + "?")


print(stutter("anything"))

# Luke, I Am Your ...
# Luke Skywalker has family and friends. Help him remind them who is who. Given a string
# with a name, return the relation of that person to Luke.


def relationToLuke(name):
    if name == "Darth Vader":
        return "Luke I am your father"
    elif name == "Leia":
        return "Luke I am your sister"
    elif name == "Han":
        return "Luke, I am your brother in law"


print(relationToLuke("Darth Vader"))

# Basic Calculator
# Create a function that takes two numbers and a mathematical operator + - / * and will
# perform a calculation with the given numbers.


def Calculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2


print(Calculator(5, "*", 5))
