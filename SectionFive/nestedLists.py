empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = [even, odd]
# this will print out [[2,4,6,8], [1,3,5,7,9]]
# you have a list within a list
print(numbers)

# will create the 2 seperate lists and print them out
for number_list in numbers:
    print(number_list)

# will print out the values inside those 2 lists
    for value in number_list:
        print(value)


menu = [
    ["eggs", "bacon"],
    ["eggs", "sausage", "bacon"],
    ["eggs", "spam"],
    ["eggs, sausage", "spam", "bacon", "spam", "tomato", "spam"],
]

# this will print only the meals that dont contain spam
for meal in menu:
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item)
    else:
        print("{0} has a spam score of {1}"
              .format(meal, meal.count("spam")))
