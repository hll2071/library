from fastapi import APIRouter
from service.book import add_book_service, get_available_books_service, delete_book_service

router = APIRouter(prefix="/books")

@router.post("")
def add_book(title: str, author: str):
    return add_book_service(title, author)

@router.get("")
def get_available_books():
    return get_available_books_service()

@router.delete("/{book_id}")
def delete_book(book_id: int):
    return delete_book_service(book_id)
