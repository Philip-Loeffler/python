class Robot(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price


class Person(object):

    def __init__(self, name, age, Robot=None):
        self.name = name
        self.age = age
        self.Robot = Robot


r1 = Robot("gary", 40)
p1 = Person("phil", 31)
print(p1.name)
p1.Robot = r1.make
print(p1.Robot)

p1.Robot = r1
print(p1.Robot.make)
