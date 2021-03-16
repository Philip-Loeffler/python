shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))

# here you can see that another list has cookies attached to it
print(another_list)

# chaining assignments
# have 8 references to the list now
a = b = c = d = e = f = another_list
print(a)
print("adding cream")
# adds another item to the list
b.append("cream")
print(c)
print(d)
