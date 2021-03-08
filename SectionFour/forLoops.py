# for loop works by iterating over sme set of values, assigning each of the values one by one to one or more variables
# then executes a block of code once for each value


parrot = "Norwegian Blue"

for character in parrot:
    print(character)


number = "9,233;372:036 854,775;807"
seperators = ""

# is numeric will return true is character is a number, or false otherwise


# fist step through of this code,
# code see's 9 as the first character in number variable, then checks if it is not numeric
# see's 9, which is numeric. since we are doing "if not" it then returns to back to the for to check again
# then looping through again, it see's a comma. so we go into the next block. so it is adding the comma
# to the seperator value, then printing it out
for char in number:
    if not char.isnumeric():
        seperators = seperators + char

print(seperators)
