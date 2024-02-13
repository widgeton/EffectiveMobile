import math
import repository as repo
import query
import show
import file


class Menu:
    page_limit = 20

    def __init__(self, repo: repo.Repository) -> None:
        self._repo = repo

    def main(self) -> repo.Repository:
        while True:
            choice = query.query_choice(query.MAIN, 5)
            match choice:
                case 0:
                    break
                case 1:
                    self._book_menu()
                case 2:
                    self._add_record_menu()
                case 3:
                    self._update_record_menu()
                case 4:
                    self._search_record_menu()
        return self._repo

    def _book_menu(self) -> None:
        page = 1
        pages = math.ceil(self._repo.get_size() / self.page_limit)
        while True:
            last = page * self.page_limit
            first = last - self.page_limit
            show.show(f"{page} из {pages}", self._repo.get_records_range(first, last))
            choice = query.query_choice(query.BOOK, 3)
            match choice:
                case 0:
                    return
                case 1:
                    if page < pages:
                        page += 1
                case 2:
                    if page > 1:
                        page -= 1

    def _add_record_menu(self) -> None:
        fields = []

        names = "Фамилия", "Имя", "Отчество", "Название организации"
        for name in names:
            nm = input(f"{name}: ").strip()
            fields.append(nm)

        phones = "Рабочий телефон", "Личный телефон"
        for phone in phones:
            phn = query.query_phone(phone)
            fields.append(phn)

        self._repo.add_records(file.record(*fields))
        print("Новая запись успешно добавлена!")

    def _update_record_menu(self):
        id_ = query.query_record_id(
            "Введите номер записи для редактирования", self._repo
        )
        print("Выбранная запись: ", id, *self._repo.get_record(id_))

        choice = query.query_choice(query.UPDATE, 7)
        match choice:
            case 0:
                return
            case 1:
                surname = input("Введите новую фамилию: ").strip().title()
                self._repo.update_record_surname(id_, surname)
            case 2:
                name = input("Введите новое имя: ").strip().title()
                self._repo.update_record_name(id_, name)
            case 3:
                middle_name = input("Введите новое отчество: ")
                self._repo.update_record_middle_name(id_, middle_name)
            case 4:
                organization = (
                    input("Введите новое название организации: ").strip()
                )
                self._repo.update_record_organization(id_, organization)
            case 5:
                work_phone = query.query_phone("Введите новый рабочий телефон")
                self._repo.update_record_work_phone(id_, work_phone)
            case 6:
                personal_phone = query.query_phone("Введите новый личный телефон")
                self._repo.update_record_personal_phone(id_, personal_phone)

        print("Запись успешно обновлена!")

    def _search_record_menu(self):
        choice = query.query_choice(query.SEARCH, 5)
        match choice:
            case 0:
                return
            case 1:
                surname = input("Введите фамилию для поиска: ").strip().title()
                records = self._repo.get_records_by_surname(surname)
            case 2:
                organization = input("Введите название организации для поиска: ").strip()
                records = self._repo.get_records_by_organization(organization)
            case 3:
                work_phone = query.query_phone("Введите рабочий телефон для поиска")
                records = self._repo.get_records_by_work_phone(work_phone)
            case 4:
                personal_phone = query.query_phone("Введите новый личный телефон")
                records = self._repo.get_records_by_personal_phone(personal_phone)

        show.show("Результаты поиска: ", records)
