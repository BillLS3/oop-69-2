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

# Объект\экземпляр на основе класса
kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 100, 1111)

kirito.action()
asuna.action()
# MageHero
# mage_hero