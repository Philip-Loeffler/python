# can multiplty
print("hello" * 5)

# the space in between the quotes is similar to concat
print("he's " "probably " "pining " "for ")

# will first do multiplication then do hello 20 times
print("hello" * (5 + 4))

# will multiply then add a four at the end
print("hello" * 5 + "4")

today = "friday"
print("day" in today)  # true
print("fri" in today)  # true
print("thurs" in today)  # false
print("parrot" in "fjord")  # false
