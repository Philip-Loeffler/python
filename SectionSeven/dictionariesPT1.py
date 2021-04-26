# unoredered, but do key valued pair, and they are accessed by keys
# cant use a list as a key
fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour yellow citrus fruit",
         "grape": "a small, sweet fruting growing in bunches",
         "lime": "a sour green citrus fruit"}
# the key is seperated by the colon
print(fruit)
# access by a key
print(fruit["lemon"])
# adding an item to a dictionary.
fruit["pear"] = "an odd shaped apple"
# doing this will update the value and get rid of the last pear string
fruit["pear"] = "great with tequila"

# to remove a key
del fruit["lemon"]
# this will clear all the items in the dictionary, and will leave an empty object
fruit.clear()
print(fruit)

# testing to see if a key is in the dictionary
print(fruit["tomato"])

# get will retrieve a key when you type it in
while True:
    dict_key = input("please enter a fruit")
    if dict_key == "quit":
        break
    # this will test if the key we type in is actually in the dictionary
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("we dont have that key" + dict_key)
