# name of this section is called class attributes

class Kettle(object):
    # this is a class attribute. all instances of the class will share this attribute
    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
hamilton = Kettle("hamilton", 14.55)

print("switch to atomic power")
# this will update the class attribute
Kettle.power_source = "atomic"
# all instances contain the class attribute "power_source"
print(Kettle.power_source)
# switching an instances attribute
print("switch kenwood to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
