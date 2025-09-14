import json
import os

DATA_FILE = "books.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_book(data, book):
    for b in data:
        if b["id"] == book["id"]:
            print("Ошибка: книга с таким ID уже существует.")
            return False
    data.append(book)
    save_data(data)
    print("Книга добавлена.")
    return True

def get_book(data, book_id):
    for book in data:
        if book["id"] == book_id:
            return book
    return None

def update_book(data, book_id, new_fields):
    for book in data:
        if book["id"] == book_id:
            book.update(new_fields)
            save_data(data)
            print("Книга обновлена.")
            return True
    print("Ошибка: книга не найдена.")
    return False

def delete_book(data, book_id):
    for i, book in enumerate(data):
        if book["id"] == book_id:
            del data[i]
            save_data(data)
            print("Книга удалена.")
            return True
    print("Ошибка: книга не найдена.")
    return False

def parse_put_command(cmd):
    parts = cmd.split(',', 4)
    print("DEBUG parts:", parts)  # это для отладки
    return {
        "id": int(parts[0].strip()),
        "title": parts[1].strip(),
        "author": parts[2].strip(),
        "date": parts[3].strip(),
        "rating": int(parts[4].strip())
    }

def main():
    data = load_data()
    print("Добро пожаловать в хранилище книг!")
    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Показать книгу по ID")
        print("3. Обновить книгу")
        print("4. Удалить книгу")
        print("5. Показать все книги")
        print("0. Выйти")

        choice = input("Выберите действие (0-5): ").strip()

        if choice == "1":
            try:
                inp = input("Введите: id, название, автор, дата, оценка через запятую:\n")
                book_data = parse_put_command(inp)
                add_book(data, book_data)
            except Exception as e:
                print("Ошибка при добавлении книги. Проверьте формат.", e)
        elif choice == "2":
            try:
                book_id = int(input("Введите id книги: "))
                book = get_book(data, book_id)
                if book:
                    print(book)
                else:
                    print("Книга не найдена.")
            except Exception:
                print("Ошибка при вводе id!")
        elif choice == "3":
            try:
                book_id = int(input("Введите id книги для обновления: "))
                print("Введите пары ключ:значение через запятую для обновления (например: title:Новое название,rating:5)")
                raw = input()
                new_data = {}
                for pair in raw.split(","):
                    key, val = pair.split(":", 1)
                    val = val.strip()
                    new_data[key.strip()] = int(val) if key.strip() in ["rating", "id"] else val
                update_book(data, book_id, new_data)
            except Exception:
                print("Ошибка в формате данных для обновления.")
        elif choice == "4":
            try:
                book_id = int(input("Введите id книги для удаления: "))
                delete_book(data, book_id)
            except Exception:
                print("Ошибка при вводе id.")
        elif choice == "5":
            print("Список всех книг:")
            for book in data:
                print(book)
        elif choice == "0":
            print("Выход.")
            break
        else:
            print("Неизвестный пункт меню!")

if __name__ == "__main__":
    main()
