from enemy import Enemy, Troll, Vampyre, VampyreKing
from player import Player

alok = Player("Alok")
# monster = Troll(name="Ogre")
monster = VampyreKing()

monster.take_damage(4)
monster.grunt()

while monster._lives > 0:
    monster.take_damage(12)
