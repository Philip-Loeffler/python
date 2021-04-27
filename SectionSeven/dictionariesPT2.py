fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour yellow citrus fruit",
         "grape": "a small, sweet fruting growing in bunches",
         "lime": "a sour green citrus fruit"}


# this is another way to achieve the same thing as in dictionary pt 1
# while True:
#     dict_key = input("please enter a fruit")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "we dont have a" + dict_key)
#     print(description)


# this is iterating over the dict
# for snack in fruit:
#     print(fruit[snack])


# for i in range(10):
#     for snack in fruit:
#         print(snack + "is" + fruit[snack])
#     print('-' + 40)

# have a list that we are storing in ordered keys
# then sorting it
# then looping over it
ordered_keys = list(fruit.keys())
ordered_keys.sort()
for f in ordered_keys:
    print(f + " - " + fruit[f])


# can also achieve with
ordered_keys = sorted(list(fruit.keys()))
for f in ordered_keys:
    print(f + " - " + fruit[f])

# can achieve with this as well

for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])

# if you dont want to sort
for f in fruit:
    print(f + " - " + fruit[f])

# for just the values
for val in fruit.values():
    print(val)

# this is far more efficent
for key in fruit:
    print(fruit[key])


fruit_keys = fruit.keys()
print(fruit_keys)
fruit["tomato"] = "not nice with ice cream"
print(fruit_keys)


print(fruit.items())
# producing a tuple
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + "is" + description)

# producing a dictionary from a tuple
print(dict(f_tuple))


# join method

# this is a poor way to join strings together
myList = ["a", "b", "c", "d"]
newString = ''
for c in myList:
    newString += c + ", "

print(newString)

# using the join method
myList = ["a", "b", "c", "d"]
newString = ", ".join(myList)
print(newString)
