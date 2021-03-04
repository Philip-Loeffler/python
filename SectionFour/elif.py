name = input("please enter your name")
# the {} are indictating where the string value from format is suppose to go
# putting int in front of input lets input know it is expecting an integer, not a string
age = int(input("how old are you? {0}".format(name)))
print(age)

if age < 18:
    print("please come back in {0} years".format(18 - age))
    # elif is is else in python
elif age == 900:
    print("sorry yoda you die in return of the jedi")
else:
    print("ehhh old enough to vote")
    print("please put an x in the box")
