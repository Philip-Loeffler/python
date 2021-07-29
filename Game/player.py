class Player(object):
    # when we create a new player object, we can pass one param, giving them a name. the other values are default values
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self.level = 1
        self.score = 0

    # underscore is suppose to represent to the user, not to call these methods
    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("lives cannot be negative")
            self._lives = 0

    lives = property(_get_lives, _set_lives)

    # the str method in python represents the class object as a string
    def __str__(self):
        return "name: {0.name}, lives: {0.lives}, level: {0.level}, score {0.score}".format(self)
