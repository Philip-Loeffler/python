# method is the same as a funciton, but it needs to be bound to an object
# when we call a methos, we tell it which object its called on
# in other words, which objecxt is should be using when it performs its function

# s.append(x)
# s = the object that we're calling the method on. in this case we append it to s
# append = the method we want to call, here it is the append method
# x = the arguments for the method. the value of x will be appeneded to the list


shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

a = b = c = d = e = f = shopping_list
print(a)
print("adding cream")

b.append("cream")
print(c)
print(d)
