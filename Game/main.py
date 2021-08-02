from player import Player
from enemy import Enemy, Troll

phil = Player("Phil")

random_monster = Enemy("basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

ugly_troll = Troll()
print("ugly troll - {}".format(ugly_troll))


another_troll = Troll("ug", 18, 1)
print("another troll - {}".format(another_troll), end="")

brother = Troll("urg", 23)
print(brother)

# overloading a method - you provide a method with exactly the same name, but with different arguements
# python doesnt have the concept of overloaded methods
