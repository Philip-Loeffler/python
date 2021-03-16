# mutables value can be changed
# pythons has these mutable objects = list, dict, set, Bytearray

# we can change the value of mutable objects, without the object being destoryed and recreated


shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

# concat another value into the shopping list
shopping_list += ["cookies"]
print(shopping_list)

# id doesnt change, because lists are mutable and python is able to add a new item to the list, without creating a new list
print(id(shopping_list))


# Strings are immutable. When we tried to change a string, python created a new object. a new string and reattached the name to it.
# immutble objects cant be changed, yo ucan create a new object and use the same variable name, but you cant change the value of an immutable object

# lists are mutable, they can be changed. when we append a new item, python was able to change the content of the list, without creating a new one
