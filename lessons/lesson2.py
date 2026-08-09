# Родительский\Супер класс
class Hero:
    # Конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибуты объекта класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
    # Методы класса
    def action(self):
        print(f"{self.name} this my base action !!")

# Дочерний класс
class MageHero(Hero):
    def action(self):
        print(f'My name {self.name} my MP')
    ...



kirito = MageHero("Kirito", 100, 1000)
asuna = Hero("Asuna", 111, 1111)
kirito.action()
asuna.action()

class Swim:
    def action(self):
        print("Swim")
class Fly:
    def action(self):
        print("Fly")
class Animal(Fly, Swim):
    # def action(self):
    #     print("Base action")
    ...
donald_duck = Animal()
# donald_duck.action()
# print(Animal.__mro__)

class A:
    def action(self):
        print("A")
class B(A):
    def action(self):
        super().action()
        print('B')
class C(A):
    def action(self):
        super().action()
        print("C")
class D(B,C):
    def action(self):
        super().action()
        print('D')

test = D()
# test.action()