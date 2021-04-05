menu = [
    ["eggs", "bacon"],
    ["eggs", "sausage", "bacon"],
    ["eggs", "spam"],
    ["eggs, sausage", "spam", "bacon", "spam", "tomato", "spam"],
]


for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]

    print(", ".join(meal))
#


flowers = [
    "Daffodil",
    "Evening primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
]

for flower in flowers:
    print(flower)

# join method will do the iterating over the list for us
seperator = " | "
output = seperator.join(flowers)
print(output)


# for all items in the iterable to be joined, they must be a string. join cannot join ints to a string
# will seperate each flower with just a comma
print(",".join(flowers))
