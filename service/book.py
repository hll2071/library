from data.book import add_book, get_available_books, delete_book

def add_book_service(title: str, author: str) -> bool:
    return add_book(title, author)

def get_available_books_service():
    books = get_available_books()
    return [{"title": book[0], "author": book[1]} for book in books]

def delete_book_service(book_id: int) -> bool:
    return delete_book(book_id)
