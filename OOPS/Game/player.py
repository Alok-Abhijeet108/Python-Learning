class Player(object):
    def __init__(self, name) -> None:
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        print("aa raha hai lives", lives)
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives can't be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        print("aa raha hai", level)
        if level >= 1:
            self.score += (level - self._level) * 1000
            self._level = level
        else:
            print("Level can't go below 1")
            self._level = 1
            self.score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if score > 0:
            self._score = score
        else:
            print("Score can't be negative")
            self._score = 0

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)
    # score = property(_get_score, _set_score)

    def __str__(self) -> str:
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)
