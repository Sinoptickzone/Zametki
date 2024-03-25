import datetime
import json
import os
import uuid


# Creates note in a specific format
def create_note():
    # Create a datetime object
    date = datetime.datetime.now()
    # Convert and split the datetime object to a strings in a specific format
    date_str = date.strftime("%d-%m-%Y")
    time_str = date.strftime("%H:%M:%S")
    # Create a uuid object
    itemid = uuid.uuid4()
    # Convert the uuid object to a string
    itemid_str = str(itemid)
    title = input("Введите заголовок заметки: ")
    content = input("Введите текст заметки: ")
    note = {"id": itemid_str, "title": title, "content": content, "date": date_str, "time": time_str}
    return note


# Writes a note to a file with a new title; if there was a note with this title, the text is updated.
def save_note(note):
    with open("notes.json", "r") as file:
        notes = [json.loads(line) for line in file]

    for item in notes:
        if item["title"] == note.get("title"):
            print("Заметка с таким заголовком уже существует. Изменяем текст.")
            delete_note(item["title"])

    with open("notes.json", "a") as file:
        json.dump(note, file)
        file.write("\n")


# Changes a note with given title, if there was one
def change_note(title):
    with open("notes.json", "r") as file:
        notes = [json.loads(line) for line in file]

    for item in notes:
        if item["title"] == title:
            print("Заметка найдена. Введите новый заголовок и текст.")
            delete_note(title)
            note = create_note()
            save_note(note)
            return
    return print("Заметка не найдена.")


# Deletes a note with given title, if there was one
def delete_note(title):
    with open("notes.json", "r") as file:
        notes = [json.loads(line) for line in file]

    for item in notes:
        if item["title"] == title:
            filtered_notes = [note for note in notes if note["title"] != title]
            with open("notes.json", "w") as file:
                for note in filtered_notes:
                    json.dump(note, file)
                    file.write("\n")
            return
    return print("Заметка не найдена.")


# Displays a list of notes from a file
def display_notes():
    with open("notes.json", "r") as file:
        for line in file:
            note = json.loads(line)
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['content']}")
            print()


# Displays a list of notes from a file on a specific day.
def filter_notes(date_filter):
    count = 0
    with open("notes.json", "r") as file:
        for line in file:
            note = json.loads(line)
            if note["date"] == date_filter:
                print(f"Заголовок: {note['title']}")
                print(f"Текст: {note['content']}")
                print()
                count += 1
        if count == 0:
            print("Заметок на указанную дату нет")


# Checks the path to the file
def where_json(file_name):
    return os.path.exists(file_name)


while True:
    print("1. Создать заметку")
    print("2. Показать все заметки")
    print("3. Удалить заметку")
    print("4. Изменить заметку")
    print("5. Показать заметки на выбранную дату")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if where_json("notes.json"):
        pass
    else:
        with open("notes.json", "w") as file:
            pass
    if choice == "1":
        note = create_note()
        save_note(note)
    elif choice == "2":
        display_notes()
    elif choice == "3":
        title = input("Введите заголовок заметки для удаления: ")
        delete_note(title)
    elif choice == "4":
        title = input("Введите заголовок заметки для изменения: ")
        change_note(title)
    elif choice == "5":
        date_filter = input("Введите дату, в формате 25-01-1999: ")
        filter_notes(date_filter)
    elif choice == "0":
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")
