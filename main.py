book_name = ''

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books_list = []
        self.reserved_books = []

    # Knygos pridėjimas į biblioteką
    def add_new_book(self, title, author, year):
        books = Book(title, author, year)
        self.books_list.append(books)

     # Knygos rezervavimas
    def resevation(self):
        reserv_lists = (bookName for bookName in self.books_list if bookName.title == book_name)

        for sezerv_books in reserv_lists:
            self.reserved_books.append(sezerv_books)
            self.books_list.remove(sezerv_books)

    # Knygos grąžinimas į biblioteką
    def returnBook(self):
        retun_book = (bookName for bookName in self.reserved_books if bookName.title == book_name)

        for retu_books in retun_book:
            self.reserved_books.remove(retu_books)
            self.books_list.append(retu_books)

    # Ieškoti knygų bibliotekoje ir rezervacijoje
    def find_books(self):
        self.books_list.sort(key=lambda x: x.year, reverse=True)
        self.reserved_books.sort(key=lambda x: x.year, reverse=True)

        find_library_book = (bookName for bookName in self.books_list if bookName.title == book_name)
        find_seserved_book = (bookName for bookName in self.reserved_books if bookName.title == book_name)
        print("Books in library")
        for library_books in find_library_book:
            print(f'Book tile:{library_books.title} -- Author: {library_books.author} -- Year: {library_books.year}')
        print("Reserved book")
        for reversed_books in find_seserved_book:
            print(f'Book tile:{reversed_books.title} -- Author: {reversed_books.author} -- Year: {reversed_books.year}')
#
#
library = Library()

while True:
    choise = input("1 - Add book to library\n2 - Reserve a book\n3 - Return The book\n4 - Books list\n5 - stop program ")
    if choise == "1":
        title = input(str('Book tile '))
        author = input(str('Author '))
        year = int(input('Year '))
        library.add_new_book(title, author, year)
    if choise == "2":
        choise = input("Reserved book title ")
        book_name = choise
        library.resevation()
    if choise == "3":
        choise = input("Return book ")
        book_name = choise
        library.returnBook()
    if choise == "4":
        choise = input("Find book: title or author ")
        book_name = choise
        library.find_books()
    if choise == "5":
        break







