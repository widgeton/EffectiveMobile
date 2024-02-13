import file
from repository import Repository
from menu import Menu

file_path = "phonebook.csv"

users = file.read(file_path)
menu = Menu(Repository(users))

repo = menu.main()

file.write(repo.get_records(), file_path)
