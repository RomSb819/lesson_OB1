#Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
#Требования:
#1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
#2.Класс `Admin`: Этот класс должен наследоваться от класса `User`. Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы `add_user` и `remove_user`, которые позволяют добавлять и удалять пользователей из списка
# (представь, что это просто список экземпляров `User`).
#3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).
#В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с реализацией задания.

class User:
    def __init__(self, user_id, name):
        self._name = name
        self._user_id = user_id
        self._access = "user"

    def get_name(self):
        return self._name
    def get_user_id(self):
        return self._user_id
    def get_access(self):
        return self._access


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access = "admin"

    def add_user(self, users, user_id, name):
        # проверка уникальности ID
        for u in users:
            if u.get_user_id() == user_id:
                return False  # такой ID уже есть

        users.append(User(user_id, name))
        print(f'Пользователь с именем {name} добавлен. Его id: {user_id}')
        return True

    def remove_user(self, users, user_id):
        for i, u in enumerate(users):
            if u.get_user_id() == user_id:
                del users[i]
                print(f"Пользователь с id: {user_id} удален")
                return True
        return False

    def show_users(self, users):
        print("\nЭто список пользователей:")
        for user in users:
            print(f"Пользователь: {user.get_name()}, id: {user.get_user_id()}, access: {user.get_access()}")

users = []

admin = Admin("001","Петр")
users.append(admin)

add_user = admin.add_user(users, "002","Ваня")
add_user = admin.add_user(users, "003", "Сеня")
remove_user = admin.remove_user(users, "003")
show_users = admin.show_users(users)



