a = b = c = d = e = f = 12
# all values bound to 12
print(c)

# unpacking a tuple
x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("unpacking a tuple")
# data represents a tuple
data = 1, 2, 76
x, y, z = data
print(x)
print(y)
print(z)


print("unpacking a list")

data_list = [12, 13, 14]
# this will crash, the list only expects 3 values. you cant append items to tuples
data_list.append(15)
p, q, r = data_list
print(p)
print(q)
print(r)


for index, character in enumerate("abcdefgh"):
    print(index, character)


for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)

index, character = (0, 'a')
print(index)
print(character)
