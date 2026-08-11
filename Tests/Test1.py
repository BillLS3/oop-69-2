from abc import ABC, abstractmethod


class Hero(ABC):
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    @abstractmethod
    def action(self):
        pass


class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        print(f"Маг {self.name} кастует заклинание! MP: {self.mp}")


class WarriorHero(MageHero):
    def __init__(self, name, lvl, hp, mp, strength):
        super().__init__(name, lvl, hp, mp)
        self.strength = strength

    def action(self):
        print(f"Воин {self.name} рубит мечом! Уровень: {self.lvl}")


class BankAccount:
    bank_name = "Simba"

    def __init__(self, hero, balance):
        self.hero = hero
        self._balance = balance
        self.__password = "1234"

    def login(self, password):
        return self.__password == password

    @property
    def full_info(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            return self._balance + other._balance
        else:
            raise TypeError("Нельзя сложить счета героев разных классов!")

    def __eq__(self, other):
        return type(self.hero) == type(other.hero) and self.hero.lvl == other.hero.lvl



try:
    h = Hero("test", 1, 1)
except TypeError as e:
    print(f"Hero нельзя создать напрямую: {e}")

mage1 = MageHero("Merlin", 50, 100, 150)
mage2 = MageHero("Gandalf", 50, 120, 200)
warrior = WarriorHero("Conan", 50, 150, 50, 100)

mage1.action()
warrior.action()

acc1 = BankAccount(mage1, 5000)
acc2 = BankAccount(mage2, 3000)
acc3 = BankAccount(warrior, 7000)

print(acc1)
print(acc2)
print(f"Банк: {BankAccount.get_bank_name()}")
print(f"Бонус за уровень: {acc1.bonus_for_level()} SOM")

print("\n=== Проверка __add__ ===")
try:
    print(f"Сумма счетов двух магов: {acc1 + acc2}")
except TypeError as e:
    print(e)

try:
    print(f"Сумма мага и воина: {acc1 + acc3}")
except TypeError as e:
    print(f"Ошибка: {e}")

print("\n=== Проверка __eq__ ===")
print(f"Mage1 == Mage2 ? {acc1 == acc2}")
print(f"Mage1 == Warrior ? {acc1 == acc3}")

print("\n=== Проверка инкапсуляции ===")
print(f"Пароль верный: {acc1.login('1234')}")
print(f"Пароль неверный: {acc1.login('0000')}")
print(f"Баланс (защищенный): {acc1._balance}")
try:
    print(acc1.__password)
except AttributeError as e:
    print(f"Не удалось получить пароль: {e}")