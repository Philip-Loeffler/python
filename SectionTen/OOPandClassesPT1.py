# this section describes that everything in python is an object. and shows how we define an object,
# and also create new instances of that object
class Kettle(object):
    # class is a template for objects to be created
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


# instance, is just an object being created from a class
# kenwood is an instanxe of the kettle class
kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

# here is another instance
hamilton = Kettle("hamilton", 14.55)
print(hamilton)


print("models: {} = {}, {} = {}".format(kenwood.make,
                                        kenwood.price, hamilton.make, hamilton.price))
