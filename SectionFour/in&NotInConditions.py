parrot = "Norweigian blue"

letter = input("enter a character: ")

# checking to see if a letter is in parrot
if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("i dont need that letter")

# here is using not


activity = input("What would you like to do today ")

# checking to see if cinema is in the activity variable. this is also case sensitive
if "cinema" not in activity.casefold():
    print("But i want to go to the cinema")
