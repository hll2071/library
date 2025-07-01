from . import con, cur

def borrow_book(book_id: int, borrower: str) -> bool:
    try:
        sql = "UPDATE books SET available = 0 WHERE book_id = ? AND available = 1"
        cur.execute(sql, (book_id,))
        if cur.rowcount == 0:
            return False
        sql = "INSERT INTO borrowings (book_id, borrower) VALUES (?, ?)"
        cur.execute(sql, (book_id, borrower))
        con.commit()
        return True
    except Exception:
        return False

def get_borrowed_books_by_month(borrow_month: str):
    sql = ("SELECT b.borrower, bk.title, bk.author "
           "FROM borrowings b "
           "JOIN books bk ON b.book_id = bk.book_id "
           "WHERE strftime('%m', b.borrowed_at) = ?")
    cur.execute(sql, (borrow_month,))
    return cur.fetchall()

def return_book(book_id: int, borrower: str) -> bool:
    try:
        sql = "UPDATE books SET available = 1 WHERE book_id = ?"
        cur.execute(sql, (book_id,))
        sql = "UPDATE borrowings SET returned_at = current_timestamp WHERE book_id = ? AND borrower = ?"
        cur.execute(sql, (book_id, borrower))
        con.commit()
        return cur.rowcount > 0
    except Exception:
        return False
