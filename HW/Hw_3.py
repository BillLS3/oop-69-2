from abc import ABC, abstractmethod
import random


class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1

    def get_health(self):
        return self.__health

    @abstractmethod
    def attack(self):
        pass


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name} атакует мечом")
        self.strength -= 1


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name} использует магию")
        self.strength -= 1


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name} атакует из-под тишка")
        self.strength -= 1


def determine_winner(player, enemy):
    if player.__class__ == Warrior:
        if enemy.__class__ == Assassin:
            return player
        elif enemy.__class__ == Mage:
            return enemy
        else:
            return None
    elif player.__class__ == Mage:
        if enemy.__class__ == Warrior:
            return player
        elif enemy.__class__ == Assassin:
            return enemy
        else:
            return None
    elif player.__class__ == Assassin:
        if enemy.__class__ == Mage:
            return player
        elif enemy.__class__ == Warrior:
            return enemy
        else:
            return None


warrior = Warrior("Артур", 5, 100, 20, 50)
mage = Mage("Гендальф", 8, 80, 15, 100)
assassin = Assassin("Эцио", 6, 90, 25, 90)

print("=" * 50)
print("🎮 Добро пожаловать в игру 'Камень, Ножницы, Бумага'!")
print("=" * 50)

while True:
    print("\nВыберите своего героя:")
    print("1 - Warrior (Воин)")
    print("2 - Mage (Маг)")
    print("3 - Assassin (Ассасин)")

    choice = input("Ваш выбор (1/2/3): ").strip()

    if choice == "1":
        player = warrior
        player_class = "Warrior"
        break
    elif choice == "2":
        player = mage
        player_class = "Mage"
        break
    elif choice == "3":
        player = assassin
        player_class = "Assassin"
        break
    else:
        print("Неверный ввод! Пожалуйста, выберите 1, 2 или 3.")

enemies = [warrior, mage, assassin]
enemy = random.choice(enemies)

if isinstance(enemy, Warrior):
    enemy_class = "Warrior"
elif isinstance(enemy, Mage):
    enemy_class = "Mage"
elif isinstance(enemy, Assassin):
    enemy_class = "Assassin"

print("\n" + "=" * 50)
print(f"Вы выбрали: {player_class} ({player.name})")
print(f"Противник: {enemy_class} ({enemy.name})")
print("=" * 50)

print("\nХарактеристики вашего героя:")
player.greet()
print(f"Здоровье: {player.get_health()}, Сила: {player.strength}")

if isinstance(player, Warrior):
    print(f"Выносливость: {player.stamina}")
elif isinstance(player, Mage):
    print(f"Мана: {player.mana}")
elif isinstance(player, Assassin):
    print(f"Скрытность: {player.stealth}")

print("\nНачинается бой!")
print("-" * 50)

print("Ваш герой атакует:")
player.attack()

print("\nПротивник атакует:")
enemy.attack()

winner = determine_winner(player, enemy)

print("\n" + "=" * 50)
print("РЕЗУЛЬТАТ БОЯ:")
print("-" * 50)

if winner is None:
    print("Ничья! Силы равны!")
elif winner == player:
    print(f"{player_class} победил! {player.name} одержал победу над {enemy.name}!")
else:
    print(f"{enemy_class} победил! {enemy.name} оказался сильнее!")
    print("Вы проиграли. Попробуйте еще раз!")

print("=" * 50)

print("\nГерои отдыхают после боя:")
player.rest()
enemy.rest()

print(f"\n{player.name}: здоровье восстановлено до {player.get_health()}")
print(f"{enemy.name}: здоровье восстановлено до {enemy.get_health()}")