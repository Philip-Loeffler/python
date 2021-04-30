locations = {0: "You are sitting in front of a computer learning python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are innside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

# converted from a list to a dictionary
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

namedExits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
              2: {"5": 5},
              3: {"1": 1},
              4: {"1": 1, "2": 2},
              5: {"2": 2, "1": 1}}

vocabulary = {"QUIT":   "Q",
              "NORTH":  "N",
              "SOUTH":  "S",
              "EAST":   "E",
              "WEST":   "W",
              "ROAD":   "1",
              "HILL":   "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}


# split function
# split is the opposite of join
print(locations[0].split())
print(locations[3].split("."))
print(''.join(locations[3].split(".")))


loc = 1
while True:
    # can use this one line of code instead of the three below
    availableExits = ", ".join(exits[loc].keys())
    # availableExits = ""
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "
    print(locations[loc])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])
    direction = input("Available exits are" + availableExits).upper()
    print()
    # pass the user input, using our vocabular dictionary if necessary
    # if more than one letter, check vocab
    if len(direction) > 1:
        # checking to see if contains a word we know?
        for word in vocabulary:
            if word in direction:
                direction = vocabulary[word]

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("you cannot go in that direction")

# doing the code with the split function
loc = 1
while True:
    # can use this one line of code instead of the three below
    availableExits = ", ".join(exits[loc].keys())
    # availableExits = ""
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "
    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are" + availableExits).upper()
    print()
    # pass the user input, using our vocabular dictionary if necessary
    # if more than one letter, check vocab
    # using split is searching what the user typed to compare
    # the other way is searching through the entire vocabulary
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("you cannot go in that direction")
