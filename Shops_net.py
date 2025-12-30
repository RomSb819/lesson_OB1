#1. Создай класс `Store`:
#-Атрибуты класса:
#- `name`: название магазина.
#- `address`: адрес магазина.
#- `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
#- Методы класса:
#- `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
#-  метод для добавления товара в ассортимент.
#- метод для удаления товара из ассортимента.
#- метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
#- метод для обновления цены товара.
#2. Создай несколько объектов класса `Store`:
#Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
#3. Протестировать методы:
#Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.
#В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с реализацией задания.

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Вы добавили '{item_name}': {price}")

    def remove_item(self, item_name):
        if item_name in self.items:
            self.items.pop(item_name, None)
            print(f"Вы удалили {item_name} за магазина {self.name}")
        else:
            print("Такого товара в магазине нет")

    def display_price(self, item_name):
        price = self.items.get(item_name)
        if price is None:
            print("Такого товара нет")
        else:
            print(f"В магазине {self.name} цена товара '{item_name}': {price}")
            return price

    def price_update(self, item_name, price):
        if item_name not in self.items:
            print("Вы ввели товар, которого нет в магазине")
        else:
            self.items[item_name] = price
            print(f"Вы обновили цену '{item_name}': {price}")

store1 = Store("Универсам", "проспект Мира, 1")
store2 = Store("555 магазин", "проспект Ленина, 25")
store3 = Store("777 магазин", "улица Колхозная, 5")

store1.add_item("Хлеб", 70)
store2.add_item("Хлеб", 75)
store3.add_item("Яблоки", 150)

store1.remove_item("Хлеб")
store2.price_update("Хлеб", 100)
store3.display_price("Яблоки")


