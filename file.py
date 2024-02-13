import csv
from collections import namedtuple
from pathlib import Path
from typing import Sequence


record = namedtuple(
    "Record", "surname, name, middle_name, organization, work_phone, personal_phone"
)


def read(file_path: str) -> list[record]:
    if _is_file_rigth(file_path):
        with open(file_path, "r", encoding="UTF-8", newline="") as file:
            reader = [*csv.reader(file)]
            if _is_fields_right(reader[0]):
                return [record(*vals) for vals in reader[1:]]
            else:
                raise ValueError("There are inaproppriated fields in file!")
    else:
        raise ValueError("Path of the file or its format is wrong.")


def _is_file_rigth(file_path: str) -> bool:
    path = Path(file_path)
    return path.is_file() and path.suffix == ".csv"


def _is_fields_right(fields: Sequence[str]) -> bool:
    return record._fields == tuple(fields)


def write(users: list[record], file_path: str) -> None:
    with open(file_path, "w", encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(record._fields)
        writer.writerows(users)
