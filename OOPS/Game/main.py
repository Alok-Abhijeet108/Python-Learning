from enemy import Enemy, Troll, Vampyre
from player import Player

alok = Player("Alok")
# monster = Troll(name="Ogre")
monster = Vampyre("Vlad")

monster.take_damage(4)
monster.grunt()

while monster.lives > 0:
    if not monster.dodges():
        monster.take_damage(3)
