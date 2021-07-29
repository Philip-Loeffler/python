from player import Player

phil = Player("Phil")

print(phil.name)
print(phil.lives)
phil.lives -= 1
print(phil)

phil.lives -= 1
print(phil)

phil.lives -= 1
print(phil)

phil.lives -= 1
print(phil)

phil._lives = 9
print(phil)

phil.level = 10
print(phil)
