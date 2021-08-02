from player import Player
from enemy import Enemy

phil = Player("Phil")

random_monster = Enemy("basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)
