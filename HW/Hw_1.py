class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает…")
        self.health += 1


# Создаем двух героев
hero1 = Hero("Артур", 5, 100, 20)
hero2 = Hero("Мерлин", 8, 80, 15)


print("=== Герой 1: Артур ===")
print(f"Начальные параметры: здоровье={hero1.health}, сила={hero1.strength}")
hero1.greet()
hero1.attack()
hero1.rest()
print(f"После действий: здоровье={hero1.health}, сила={hero1.strength}")
print()


print("=== Герой 2: Мерлин ===")
print(f"Начальные параметры: здоровье={hero2.health}, сила={hero2.strength}")
hero2.greet()
hero2.attack()
hero2.rest()
print(f"После действий: здоровье={hero2.health}, сила={hero2.strength}")