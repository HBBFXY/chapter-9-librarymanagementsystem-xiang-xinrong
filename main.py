class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def check_availability(self):
        return not self.is_borrowed

    def borrow(self):
        if self.check_availability():
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

class User:
    def __init__(self, name, card_id):
        self.name = name
        self.card_id = card_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

if __name__ == "__main__":
    lib = Library()
    book1 = Book("Python编程", "张三", "9787115546081")
    book2 = Book("数据结构", "李四", "9787040556680")
    lib.add_book(book1)
    lib.add_book(book2)

    user1 = User("小明", "U001")
    lib.add_user(user1)

    user1.borrow_book(lib.find_book_by_isbn("9787115546081"))
    print(book1.check_availability())
    user1.return_book(lib.find_book_by_isbn("9787115546081"))
    print(book1.check_availability())
