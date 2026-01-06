# Задание: Разработать консольную игру "Битва героев" на Python с использованием классов и разработать план проекта по этапам/или
# создать kanban доску для работы над данным проектом
# # Общее описание:
# # Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с различными характеристиками.
# Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.
# # Требования:
# # 1. Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# # 2. Игра должна быть реализована как консольное приложение.
# # Классы:
# # Класс `Hero`:
# # - Атрибуты:
# # - Имя (`name`)
# # - Здоровье (`health`), начальное значение 100
# # - Сила удара (`attack_power`), начальное значение 20
# # - Методы:
# # - `attack(other)`: атакует другого героя (`other`), отнимая здоровье в размере своей силы удара
# # - `is_alive()`: возвращает `True`, если здоровье героя больше 0, иначе `False`
# # Класс `Game`:
# # - Атрибуты:
# # - Игрок (`player`), экземпляр класса `Hero`
# # - Компьютер (`computer`), экземпляр класса `Hero`
# # - Методы:
# # - `start()`: начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет. Выводит информацию о каждом ходе
# (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.
# # # В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с реализацией задания и скриншот/файл с планом
# проекта по этапам или kanban-доску (таблицу/скриншот таблицы)

import random

class Hero():
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        if other.health <= 0:
            other.health = 0
        return other.health

    def is_alive(self):
        if self.health <= 0:
            return False
        else:
            return True

class Game():
    def __init__(self, player : Hero, computer : Hero):
        self.player = player
        self.computer = computer

    def start_game(self, player, computer):
        while True:
            self.computer.is_alive()
            self.player.is_alive()

            self.player.attack(self.computer)
            print(f'{self.player.name} атаковал {self.computer.name}, здоровья осталось {self.computer.health}')
            if self.computer.is_alive() is False:
                print("Игрок победил")
                break


            self.computer.attack(self.player)
            print(f'{self.computer.name} атаковал {self.player.name}, здоровья осталось {self.player.health}')
            if self.player.is_alive() is False:
                print("Компьютер победил")
                break

game_round = 3

for i in range(game_round):
    player1 = Hero("Игрок 1", 10, random.randint(1, 5))
    computer1 = Hero("Компьютер 1", 10, random.randint(1, 5))
    game = Game(player1, computer1)

    print(f"Раунд {i+1}")
    game.start_game(player1, computer1)

