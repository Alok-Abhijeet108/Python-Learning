import random


class Enemy:
    def __init__(self, name="Enemy", hit_points=0, lives=1) -> None:
        self.name = name
        self.base_hit_points = hit_points
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print(f"I took {damage} points damage and have {remaining_points} left")
        else:
            self.lives -= 1
            if self.lives > 0:
                self.hit_points = self.base_hit_points
                print("Ha ha ha ! I'm immortal")
            else:
                self.hit_points = 0
                print("Urgh! I'm defeated at last")
        print(self)

    def __str__(self) -> str:
        return "Name: {0.name}, Lives: {0.lives}, Hit points: {0.hit_points}".format(self)


class Troll(Enemy):
    def __init__(self, name="Troll") -> None:
        super().__init__(name=name, hit_points=23, lives=1)

    def grunt(self):
        print(f"Me {self.name}, {self.name} stomp you")


class Vampyre(Enemy):
    def __init__(self, name="Dracula") -> None:
        super().__init__(name=name, hit_points=12, lives=3)

    def grunt(self):
        print(f"I am {self.name}, gimme your blood")

    def dodges(self):
        if random.randint(1, 3) == 3:
            print(f"**** {self.name} dodges ****")
            return True
        else:
            return False
