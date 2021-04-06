# a tuple is a mathematcial name for an ordered set of data
# in python, tuples are another sequence type; along with strings, lists and ranges, that we have already seen
# tuples differe from lists because tuples are immutable. that means they cannot be changed after
# they are created. just likes strings.
#
# tuples protect integrity of data
# we tried to change the meallica name at index 0, and in this case it didnt work
# you can tell if its a tuple because its in parans when you print it
t = ("a", "b", "c")
print(t)


name = "tim"
age = 10

print(name, age, "python", 2021)

# this turns it into a tuple
print((name, age, "python", 2021))

# sequenced type, so we an use sequencing
welcome = "Welcome to my nightmare", "alice cooper", 1975
bad = "bad company", "bad company", 1974
budgie = "nightflight", "budgie", 1981
imelda = "more mayhem", "emilda may", 2011
metallica = "ride the lignting", "metallica", 1986

print(metallica)

# sequenced type, so we an use indexing
print(metallica[0])

# so this wont work because they are immutable. they cannot be changed after they are created
metallica[0] = "master of puppets"


# this will turn out tuple into a list, so it will have square brackets, and we can change the title
metallica2 = list(metallica)
print(metallica2)
metallica2[0] = "master of puppets"
# advantages of tuples:
# using a tuple, for things that shouldnt change, can help to prevent bugs in your program
# if you code attempts to change one of the fields in a tuple, your code will fail, that will
# highlight something that your code probably should not be doing

title, artist, year = metallica
print(title)
print(artist)
print(year)

table = ("coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])

# unpack the tuple into variables and using those variable names into our code
name, length, width, height, price = table
print(length * width)
