class Player(object):
    # when we create a new player object, we can pass one param, giving them a name. the other values are default values
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self.score = 1000

    # underscore is suppose to represent to the user, not to call these methods
    # it also hides the attribute
    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("lives cannot be negative")
            self._lives = 0

    lives = property(_get_lives, _set_lives)

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self.score += delta * 1000
            self._level = level
        else:
            print("level cant bne less than 1")

    # the str method in python represents the class object as a string
    # if you were to call the object: print("whatever the variable is")
    # it will return that object with the values of its properties

    level = property(_get_level, _set_level)

    def __str__(self):
        return "name: {0.name}, lives: {0.lives}, level: {0.level}, score {0.score}".format(self)
