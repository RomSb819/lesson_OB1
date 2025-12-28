#Менеджер задач

#Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
#У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
#Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

from datetime import datetime, date

class Task:
    def __init__(self):
        # Здесь хранятся все задачи
        self.tasks = []

    def add(self, description: str, deadline_str: str):
        try:
            deadline = datetime.strptime(deadline_str, "%d.%m.%Y").date()
        except ValueError:
            print("Ошибка: дата должна быть в формате ДД.ММ.ГГГГ (например 28.12.2025)")
            return
        self.tasks.append({
            "description": description,
            "deadline": deadline,
            "completed": False
        })
        print("✅ Задача добавлена!")

    def complete(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print("✅ Задача отмечена как выполненная!")
        else:
            print("Ошибка: нет задачи с таким номером.")

    def show_uncompleted(self):
       # Показать все невыполненные задачи
        print("\n Текущие (невыполненные) задачи:")
        has_tasks = False

        for i, task in enumerate(self.tasks):
            if not task["completed"]:
                deadline = task["deadline"].strftime("%d.%m.%Y")
                print(f"{i}. {task['description']} | Срок: {deadline}")
                has_tasks = True

        if not has_tasks:
            print("Нет текущих задач!")

    def show_done(self):
       # Показать все сделанные задачи
        print("\n Выполенные задачи:")
        has_tasks = False

        for i, task in enumerate(self.tasks):
            if  task["completed"]:
                deadline = task["deadline"].strftime("%d.%m.%Y")
                print(f"{i}. {task['description']} | Срок: {deadline}")
                has_tasks = True

        if not has_tasks:
            print("Нет выполненных задач!")

    def run_menu(self):
        # Запуск меню для пользователя
        while True:
            print("\n--- МЕНЮ ---")
            print("1) Добавить задачу")
            print("2) Отметить задачу выполненной")
            print("3) Показать текущие задачи")
            print("4) Показать выполенные задачи")
            print("5) Выход")

            choice = str(input("Выбери пункт (1-5): "))

            if choice == "1":
                desc = str(input("Введите описание задачи: "))
                deadline = str(input("Введите срок (ДД.ММ.ГГГГ): "))
                self.add(desc, deadline)

            elif choice == "2":
                num_str = str(input("Введите номер задачи: "))
                if num_str.isdigit():
                    self.complete(int(num_str))
                else:
                    print("Ошибка: нужно ввести число.")

            elif choice == "3":
                self.show_uncompleted()

            elif choice == "4":
                self.show_done()

            elif choice == "5":
                print("Пока!")
                break

            else:
                print("Ошибка: выбери число от 1 до 5.")


if __name__ == "__main__":
    tasks = Task()
    tasks.run_menu()
