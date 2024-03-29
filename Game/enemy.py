# fun fact, enemy is technically a subclass because all classes inherit from object
# so you could write it like, class Enemy(object): for all you technical folk out there
class Enemy:

    def __init__(self, name="enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("i took {} points damage and have {} left".format(
                damage, self.hit_points))
        else:
            self.lives -= 1

    def __str__(self):
        return "name: {0.name}, lives: {0.lives}, hit points: {0.hit_points}".format(self)


# this is how you create a subclass. Troll is inheriting from enemy
class Troll(Enemy):
    # when you create a troll object, you will give it a specific name.
    # and the lives and hit points will be added to it from the super class
    # because of the super class init method in the subclass
    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("me {0.name}. {0.name} stomp you".format(self))
