
# split method splits a string up into words

panagram = """the quick brown 
fox jumps\tover the lazy dog"""

# returns a list split by comma's
words = panagram.split()
print(words)


numbers = "9,223,372,036,775,807"

print(numbers.split(","))

# use a for loop to produce a list of ints, rather than strings
# loops through the value list
# value_list at index 0 is going to be equal to valuelist at index 0 which is being converted to an int
# so valuelist at index 0 is now the string at value 0 converted into an int
# badabing you now have an int at value list index 0
for index in range(len(values_list))
values_list[index] = int(values_list[index])

print(values_list)


# second method with appending
# creating a new list, then appending the values to a new list
integer_values = []
for value in values_list:
    integer_values.append(int(values))
print(integer_values)
