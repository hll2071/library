from . import con, cur

def add_book(title: str, author: str) -> bool:
    try:
        sql = "INSERT INTO books (title, author) VALUES (?, ?)"
        cur.execute(sql, (title, author))
        con.commit()
        return True
    except Exception:
        return False

def get_available_books():
    sql = "SELECT title, author FROM books WHERE available = 1"
    cur.execute(sql)
    return cur.fetchall()

def delete_book(book_id: int) -> bool:
    try:
        sql = "DELETE FROM books WHERE book_id = ? AND available = 1"
        cur.execute(sql, (book_id,))
        con.commit()
        if cur.rowcount > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error deleting book: {e}")
        return False
