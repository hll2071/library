from data.borrowings import borrow_book, get_borrowed_books_by_month, return_book
from cache.borrower import save_borrowed_book, get_borrowed_books, remove_borrowed_book

def borrow_book_service(book_id: int, borrower: str, title: str) -> bool:
    if borrow_book(book_id, borrower):
        save_borrowed_book(borrower, title)
        return True
    return False

def get_borrowed_books_by_month_service(borrow_month: str):
    records = get_borrowed_books_by_month(borrow_month)
    return [{"borrower": record[0], "title": record[1], "author": record[2]} for record in records]

def get_borrowed_books_service(borrower: str):
    books = get_borrowed_books(borrower)
    return {"borrower": borrower, "books": list(books)}

def return_book_service(book_id: int, borrower: str, title: str) -> bool:
    if return_book(book_id, borrower):
        remove_borrowed_book(borrower, title)
        return True
    return False
