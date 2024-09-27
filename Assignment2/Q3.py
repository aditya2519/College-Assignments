import datetime

# Sample book data
books_data = [
    {"title": "Book A", "author": "Author 1", "checked_out": True, "due_date": "2024-09-20"},
    {"title": "Book B", "author": "Author 2", "checked_out": False, "due_date": None},
    {"title": "Book C", "author": "Author 3", "checked_out": True, "due_date": "2024-09-25"},
    {"title": "Book D", "author": "Author 1", "checked_out": False, "due_date": None},
    {"title": "Book E", "author": "Author 2", "checked_out": True, "due_date": "2024-09-15"},
]

# 1. Total number of available (not checked out) books
available_books = [book for book in books_data if not book["checked_out"]]

# 2. Most borrowed books (we'll simulate the count as not present in this data)
# Assuming a dictionary with counts for each book (based on title for simplicity)
borrow_count = {"Book A": 5, "Book B": 2, "Book C": 7, "Book D": 3, "Book E": 9}
most_borrowed = max(borrow_count, key=borrow_count.get)

# 3. Overdue books (due date has passed)
today = datetime.date.today()
overdue_books = [book for book in books_data if book["checked_out"] and book["due_date"] and datetime.date.fromisoformat(book["due_date"]) < today]

# Output results
print(f"Total available books: {len(available_books)}")
print(f"Most borrowed book: {most_borrowed}")
print(f"Overdue books: {[book['title'] for book in overdue_books]}")
