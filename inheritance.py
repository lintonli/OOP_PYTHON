class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_book(self):
        return  f"The title is {self.title} and author is {self.author} and year is {self.year}"


#child class that inherits book properties from the parent Book
class Library(Book):
    def __init__(self, title, author, year, book_available):
        #super is a function used to inherit
        super().__init__(title, author, year)
        self.book_available = book_available
    def borrow_book(self):
        if self.book_available > 0:
            self.book_available-=1
            return  f"{self.title} borrowed. Copies available: {self.book_available}"
        else:
            return f"{self.title} not available"
    def return_book(self):
        self.book_available+=1
        return  f"{self.title} returned. Copies available: {self.book_available}"


Book1= Library("enemy of the people", "John Kiriamity", 2002, 30)
print(Book1.display_book())
print(Book1.borrow_book())
print(Book1.return_book())