import repository as repo


CHOICES = "0", "1", "2", "3", "4", "5", "6"

MAIN = """
Введите цифру...
1 для вывода всей телефонной книги
2 для добавления записи
3 для редактирования записи
4 для поиска записи

0 для выхода
-----------------------------------
Ввод: """

BOOK = """
Введите цифру...
1 для следующей страницы
2 для предыдущей страницы

0 для возвращения в главное меню
-----------------------------------
Ввод: """

UPDATE = """
Введите цифру, если хотите отредактировать...
1 фамилию
2 имя
3 отчество
4 название организации
5 рабочий номер телефона
6 личный номер  телефона

0 для возвращения в главное меню
-----------------------------------
Ввод: """

SEARCH = """
Введите цифру для поиска...
1 по фамилии
2 по названию организации
3 по рабочему номеру телефона
4 по личному номеру телефона

0 для возвращения в главное меню
-----------------------------------
Ввод: """


def query_choice(text: str, choices: int) -> int:
    while True:
        choice = input(text).strip()
        if choice in CHOICES[: choices + 1]:
            return int(choice)
        print("Неверный ввод!")


def query_phone(text: str) -> str:
    while True:
        phn = input(f"{text}: ").strip()
        if phn.isdecimal() and len(phn) == 11 and phn.startswith("7"):
            return phn
        print("Номер должен состоять из 11 цифр с 7-кой в начале!")


def query_record_id(text: str, repo: repo.Repository) -> int:
    while True:
        id_ = input(f"{text}: ").strip()
        if id_.isdecimal() and 0 <= int(id_) < repo.get_size():
            return int(id_)
        print("Неверно введен номер записи или такого номера не существует!")
