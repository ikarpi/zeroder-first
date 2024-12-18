class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} ест.")

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} щебечет.")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} ревет.")

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит.")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Сотрудник {staff_member.name} добавлен в зоопарк")

    def display_animals(self):
        for animal in self.animals:
            print(f"{animal.name}, Возраст: {animal.age}")

    def display_staff(self):
        for staff in self.staff:
            print(f"{staff.name}, Позиция: {type(staff).__name__}")

class ZooKeeper():
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} исцеляет {animal.name}.")

bird = Bird("Попугай", 3, 50)
mammal = Mammal("Лев", 5, "белый")
reptile = Reptile("Сокол", 7, "соколинный")

zoo = Zoo()
keeper = ZooKeeper("Алекс")
veterinarian = Veterinarian("Егор")

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zoo.add_staff(keeper)
zoo.add_staff(veterinarian)

animal_sound(zoo.animals)

keeper.feed_animal(bird)
veterinarian.heal_animal(mammal)

import json

def save_zoo(zoo, filename):
    data = {
        "animals": [{"name": a.name, "age": a.age, "type": type(a).__name__} for a in zoo.animals],
        "staff": [{"name": s.name, "type": type(s).__name__} for s in zoo.staff]
    }
    with open(filename, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_zoo(filename):
    zoo = Zoo()
    with open(filename, 'r') as f:
        data = json.load(f)
        for a in data["animals"]:
            if a["type"] == "Bird":
                zoo.add_animal(Bird(a["name"], a["age"], wing_span=50))
            elif a["type"] == "Mammal":
                zoo.add_animal(Mammal(a["name"], a["age"], fur_color="белый"))
            elif a["type"] == "Reptile":
                zoo.add_animal(Reptile(a["name"], a["age"], scale_type="соколинный"))
        for s in data["staff"]:
            if s["type"] == "ZooKeeper":
                zoo.add_staff(ZooKeeper(s["name"]))
            elif s["type"] == "Veterinarian":
                zoo.add_staff(Veterinarian(s["name"]))
    return zoo
