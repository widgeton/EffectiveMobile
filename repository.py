import file


class Repository:

    def __init__(self, records: list[file.record]) -> None:
        self._records = records

    def get_records_range(
        self, fst_idx: int, lst_idx: int
    ) -> list[tuple[int, file.record]]:
        return [usr for usr in enumerate(self._records[fst_idx:lst_idx], fst_idx)]

    def get_size(self) -> int:
        return len(self._records)

    def get_records(self) -> list[file.record]:
        return self._records

    def add_records(self, user: file.record):
        self._records.append(user)

    def get_record(self, id_: int) -> file.record:
        return self._records[id_]

    def update_record_surname(self, id_: int, surname: str) -> None:
        self._records[id_] = self._records[id_]._replace(surname=surname)

    def update_record_name(self, id_: int, name: str) -> None:
        self._records[id_] = self._records[id_]._replace(name=name)

    def update_record_middle_name(self, id_: int, middle_name: str) -> None:
        self._records[id_] = self._records[id_]._replace(middle_name=middle_name)

    def update_record_organization(self, id_: int, organization: str) -> None:
        self._records[id_] = self._records[id_]._replace(organization=organization)

    def update_record_work_phone(self, id_: int, work_phone: str) -> None:
        self._records[id_] = self._records[id_]._replace(work_phone=work_phone)

    def update_record_personal_phone(self, id_: int, personal_phone: str) -> None:
        self._records[id_] = self._records[id_]._replace(personal_phone=personal_phone)

    def get_records_by_surname(self, surname: str) -> list[tuple[int, file.record]]:
        return [usr for usr in enumerate(self._records) if usr[1].surname == surname]

    def get_records_by_organization(
        self, organization: str
    ) -> list[tuple[int, file.record]]:
        return [
            usr 
            for usr in enumerate(self._records)
            if usr[1].organization == organization
        ]

    def get_records_by_work_phone(
            self, work_phone: str
        ) -> list[tuple[int, file.record]]:
        return [
            usr 
            for usr in enumerate(self._records) 
            if usr[1].work_phone == work_phone
        ]

    def get_records_by_personal_phone(
        self, personal_phone: str
    ) -> list[tuple[int, file.record]]:
        return [
            usr
            for usr in enumerate(self._records)
            if usr[1].personal_phone == personal_phone
        ]
