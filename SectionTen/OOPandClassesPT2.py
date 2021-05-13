# this section is entitled "instances, constructors, sets and more"
# class: template for creating obects. all objects created using the same class will have the same characterists
# object: an instance of a class
# instantiate: create an instance of a class
# method: a function defined in a class
# attribute: a variable bound to an instance of a class
# in python, every type is a class
# the init method is the constructor


class Kettle(object):
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

# functions that are bound to a class are called methods. and the main difference is the presence of the self parameter
# self is similar to this.on in java
# self is a reference to the instance of the class
    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
hamilton = Kettle("hamilton", 14.55)

# because kenwood and hamilton are objects, we can replace them in the attribute fields
print("models: {0.make} = {0.price}, {1.make} = {1.price}".format(
    kenwood, hamilton))

# when we run hamilton here, it will be false
print(hamilton.on)
hamilton.switch_on()
# then when we run it here, after the switch function is called, it will come back as true
print(hamilton.on)


Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print("*" * 80)
# power is bound to the instance of the kenwood class
kenwood.power = 1.5
print(kenwood.power)
# power will not be availabe on hamilton, since it hasnt been added to this instance
print(hamilton.power)
