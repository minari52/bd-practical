import json
import os

DATA_FILE = "book.json"

#загрузка данных из файла
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding="utf-8") as f:
        return json.load(f)
    
#сохранение данных в файл
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

#добавление книги
def add_book(data, book):
    for b in data:
        if b["id"] == book["id"]:
            print("ошибка: такой id уже используется")
            return False
    data.append(book)
    save_data(data)
    print("книга добавлена")
    return True
    
#получаем книгу по id
def get_book(data, book_id):
    for book in data:
        if book['id'] == book_id:
            return book
    return None
    
#изменение данных по id
def update_book(data, book_id, new_fields):
    for book in data:
        if book["id"] == book_id:
            book.update(new_fields)
            save_data(data)
            print("данные обновлены")
            return True
    
    print("ошибка: книга не найдена")
    return False

#удаление книги по id
def delet_book(data, book_id):
    for i, book in enumerate(data):
        if book["id"] == book_id:
            del data[i]
            save_data(data)
            print("книга удалена")
            return True
    
    print("ошибка: книга не найдена")
    return False

def parse_put_command(cmd):
    parts = cmd.split(',', 4)
    print("DEBUG parts:", parts)
    return {
        "id": int(parts[0].strip()),
        "title": parts[1].strip(),
        "author": parts[2].strip(),
        "data": parts[3].strip(),
        "rating": int(parts[4].strip())
    }

def main():
    data = load_data()
    print("добро пожаловать в хранилище")
    while True:
        print("\nменю:")
        print("1. добавить книгу")
        print("2. найти книгу по id")
        print("3. обновить книгу")
        print("4. удалить книгу")
        print("5. показать все книги")
        print("0. выйти")

        choice = input("выберите действие (0-5): ").strip()

        if choice == '1':
            try:
                inp = input("введите: id, название, автора, дату окончания и оценку книге через запятую:\n")
                book_data = parse_put_command(inp)
                add_book(data, book_data)
            except Exception as e:
                print("ошибка, при добавлении книги. проверьте формат", e)

        elif choice == '2':
            try:
                book_id = int(input("введите id книги:"))
                book = get_book(data, book_id)
                if book:
                    print(book)
                else:
                    print("книга не найдена")
            
            except Exception:
                print("ошибка при вводе id")

        elif choice == '3':
            try:
                book_id = int(input("введите id книги для обновления"))
                print("введите новое название, автора, дату окончания и рейтинг. например(title: новое название, rating: новый рейтинг) ")
                raw = input()
                new_data = {}
                for eclipse in raw.split(","):
                    key, val = eclipse.split(":", 1)
                    val = val.strip()
                    new_data[key.strip()] = int(val) if key.strip() in ["rating", "id"] else val
                    update_book(data, book_id, new_data)
            
            except Exception:
                print("ошибка в формате данных для обновления")
        
        elif choice == '4':
            try:
                book_id = int(input("введите id для удаления:"))
                delet_book(data, book_id)
            
            except Exception:
                print("ошибка при в воде id")

        elif choice == '5':
            print("список всех книг:")
            for book in data:
                print(book)
        
        elif choice == "0":
            print("выход")
            break
        else:
            print("неизвестный пункт в меню")

if __name__ == "__main__":
    main()
                





            

 



