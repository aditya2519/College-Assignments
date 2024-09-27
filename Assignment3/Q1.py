# Class representing a book in the library
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # Book availability status

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"

# Class representing a library member
class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []  # List to store borrowed books

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} did not borrow {book.title}.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title}")
        else:
            print(f"{self.name} has not borrowed any books.")

# Class representing the library system
class Library:
    def __init__(self):
        self.books = []  # List to store books in the library
        self.members = []  # List to store registered members

    # Add a new book to the library
    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        print(f"Added {book.title} to the library.")

    # Register a new member
    def register_member(self, name, membership_id):
        member = Member(name, membership_id)
        self.members.append(member)
        print(f"Registered {name} as a new member.")

    # List all available books in the library
    def list_available_books(self):
        available_books = [book for book in self.books if book.available]
        if available_books:
            print("Available books in the library:")
            for book in available_books:
                print(f"- {book}")
        else:
            print("No books are currently available.")

    # Find a book by its title
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        print(f"Book titled '{title}' not found.")
        return None

    # Find a member by their membership ID
    def find_member(self, membership_id):
        for member in self.members:
            if member.membership_id == membership_id:
                return member
        print(f"Member with ID '{membership_id}' not found.")
        return None

# Example usage of the system:
library = Library()

# Add books to the library
library.add_book("The Catcher in the Rye", "J.D. Salinger", "12345")
library.add_book("To Kill a Mockingbird", "Harper Lee", "67890")

# Register members
library.register_member("Aditya", "M001")
library.register_member("Kartik", "M002")

# List available books
library.list_available_books()

# Borrow and return books
member1 = library.find_member("M001")
book1 = library.find_book("The Catcher in the Rye")

if member1 and book1:
    member1.borrow_book(book1)
    member1.list_borrowed_books()

# Try to borrow a book that is already borrowed
member2 = library.find_member("M002")
if member2 and book1:
    member2.borrow_book(book1)

# Return the book and list the available books again
if member1 and book1:
    member1.return_book(book1)
    library.list_available_books()
