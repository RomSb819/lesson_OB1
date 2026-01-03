# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return print("разговаривает")

    def eat(self):
        return print("Ест")

class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        return print("Чирик-чирик")


class Mammal(Animal):
    def __init__(self, name, age, inhabitancy):
        super().__init__(name, age)
        self.inhabitancy = inhabitancy

    def make_sound(self):
        return print("Му-у")

class Reptile(Animal):
    def __init__(self, name, age, legs):
        super().__init__(name, age)
        self.legs = legs

    def make_sound(self):
        return print("Ш-ш-ш")

class Staff:
    def __init__(self, name, years_worked):
        self.name = name
        self.years_worked = years_worked

    def __repr__(self):  # Для списков и print
        return f'<{self.__class__.__name__} {self.name}>'

    def __str__(self):  # Для print(объект) — опционально
        return f'Сотрудник {self.name} (стаж {self.years_worked})'


class ZooKeeper(Staff):
    def __init__(self, name, years_worked, animal_type):
        super().__init__(name, years_worked)
        self.animal_type = animal_type
    def feed_animal(self, animal):
        animal.eat()
        return print(f'Смотритель {self.name} накормил животное {animal.name}')


class Veterinarian(Staff):
    def __init__(self, name, years_worked, specialization):
        super().__init__(name, years_worked)
        self.specialization = specialization
    def heal_animal(self, animal):
        return print(f'Ветеринар {self.name} вылечил животное {animal.name}')


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в {self.name}")

    def add_employee(self, employee):
        self.staff.append(employee)
        print(f"Сотрудник {employee.name} добавлен в {self.name}. Персонал: {len(self.staff)} чел.")

    def show_info(self):
        print(f"Зоопарк {self.name}: {len(self.animals)} животных, {len(self.staff)} сотрудников")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


workers = [ZooKeeper("Петр", 3, "птицы"), Veterinarian("Татьяна", 3, "Рептилии")]

animals = [Bird("чижик",1,"brown"), Mammal("Cow",2, "home" ), Reptile("Snake",3,0)]
animal_sound(animals)

my_zoo = Zoo("Московский зоопарк")
my_zoo.add_animal(animals[0])
my_zoo.add_animal(Bird("Чижик", 1, "brown"))
my_zoo.add_employee(workers[1])
my_zoo.add_employee(ZooKeeper("Иван", 5, "птицы"))
my_zoo.show_info()  # Работает полиморфизм и композиция
