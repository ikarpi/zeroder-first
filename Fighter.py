from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")

class Bow(Weapon):
    def attack(self):
        print("Боец делает выстрел из лука.")

class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self,new_weapon: Weapon):
        self.weapon = new_weapon

    def attack(self, monstr):
        print("Боец выбирает оружие.")
        self.weapon.attack()
        print("Монстр побежден!\n")

class Monster():
    def __init__(self, name):
        self.name = name

sword = Sword()
bow = Bow()

fighter = Fighter(sword)
monster = Monster("Дракон")

fighter.attack(monster)

fighter.change_weapon(bow)

fighter.attack(monster)































