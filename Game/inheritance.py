# inheritance - different types of objects in the "real world" can have certain amount of features common with each other
# for instance, a bird object with a beak and wing property. and eagle, crow, ostrich all have these qualities
# so they would inherit them from the bird class
# in other words, they share the "being a bird trait", so to speak. they all have a beak and wings, thing they inherit by virtue
# of them being birds.
# so what we can do is define a base class, that objects are based on, thing thats that are commone for classes
# to derive from that base class. then we can allow a call to define the unique characterists of itself.
# so all our birds inherit some basic propeties from their base class. which is often referred to as the super class
# they also inherit methods, so all our birds can walk and eat, but the individual bird classes have their own unique properties and methods
# so we would have a base class and then something that inherits from that to make it something else, making it unique
# one more example would be, monopoly the board game, blackjack the card game and halo the computer game, all are inherently games
# so they share similar properties, being a game, but they are also different
class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 1000

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("level cant bne less than 1")

    level = property(_get_level, _set_level)
    lives = property(_get_lives, _set_lives)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return "name: {0.name}, lives: {0.lives}, level: {0.level}, score {0.score}".format(self)
