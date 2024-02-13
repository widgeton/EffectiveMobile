import file


def show(text: str, records: list[tuple[int, file.record]]):
    print(text)
    for id, rcd in records:
        print(id, *rcd)
