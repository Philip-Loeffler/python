from player import Player
from enemy import Enemy, Troll

phil = Player("Phil")

random_monster = Enemy("basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

# doing this a new troll object is created with its name being blargh, and it will
# have the lives and hit points from the enemy class because the super class
# init is being called from the subclass
ugly_troll = Troll("blargh")
print("ugly troll - {}".format(ugly_troll))

ugly_troll.grunt()
