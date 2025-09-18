#2
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print()

    def discount(self, percent):
        self.price = self.price - (self.price * percent / 100)

# make two books
book1 = Book("Python Basics", "John Smith", 500)
book2 = Book("C++ Programming", "Alice Brown", 600)

print("Book 1:")
book1.show()

print("Book 2:")
book2.show()

# 10% to book2
book2.discount(10)

print("Book 2 after 10% discount:")
book2.show()
