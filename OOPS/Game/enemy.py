import random


class Enemy:
    def __init__(self, name="Enemy", hit_points=0, lives=1) -> None:
        self._name = name
        self._base_hit_points = hit_points
        self._hit_points = hit_points
        self._lives = lives

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print(f"I took {damage} points damage and have {remaining_points} left")
        else:
            self._lives -= 1
            if self._lives > 0:
                self._hit_points = self._base_hit_points
                print("Ha ha ha ! I'm immortal")
            else:
                self._hit_points = 0
                print("Urgh! I'm defeated at last")
        print(self)

    def __str__(self) -> str:
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)


class Troll(Enemy):
    def __init__(self, name="Troll") -> None:
        super().__init__(name=name, hit_points=23, lives=1)

    def grunt(self):
        print(f"Me {self._name}, {self._name} stomp you")


class Vampyre(Enemy):
    def __init__(self, name="Vlad", hit_points=12, lives=3) -> None:
        super().__init__(name=name, hit_points=hit_points, lives=lives)

    def grunt(self):
        print(f"I am {self._name}, gimme your blood")

    def dodges(self):
        if random.randint(1, 3) == 3:
            print(f"**** {self._name} dodges ****")
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class VampyreKing(Vampyre):
    def __init__(self, name="Count Dracula") -> None:
        super().__init__(name=name, hit_points=140, lives=5)

    def take_damage(self, damage):
        return super().take_damage(damage=damage // 4)
