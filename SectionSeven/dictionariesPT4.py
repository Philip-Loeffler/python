fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour yellow citrus fruit",
         "grape": "a small, sweet fruting growing in bunches",
         "lime": "a sour green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favorite",
       "sprouts": "mmm, lovely",
       "spinach": "can i have some more fruit please"}

# using the update method, we are able to combine two dicts together, passing one as a parameter

veg.update(fruit)
print(veg)


nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)
