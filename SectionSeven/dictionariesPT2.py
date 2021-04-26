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
