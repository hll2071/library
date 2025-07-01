from fastapi import APIRouter
from service.borrowings import (
    borrow_book_service, get_borrowed_books_by_month_service,
    get_borrowed_books_service, return_book_service
)

router = APIRouter(prefix="/borrows")

@router.post("")
def borrow_book(book_id: int, borrower: str, title: str):
    return borrow_book_service(book_id, borrower, title)

@router.get("/month/{borrow_month}")
def get_borrowed_books_by_month(borrow_month: str):
    return get_borrowed_books_by_month_service(borrow_month)

@router.get("/{borrower}/books")
def get_borrowed_books(borrower: str):
    return get_borrowed_books_service(borrower)

@router.post("/return")
def return_book(book_id: int, borrower: str, title: str):
    return return_book_service(book_id, borrower, title)
