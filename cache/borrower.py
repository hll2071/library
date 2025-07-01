from cache import redis_client

def save_borrowed_book(borrower: str, title: str):
    key = f"borrower:{borrower}:books"
    redis_client.sadd(key, title)

def get_borrowed_books(borrower: str):
    key = f"borrower:{borrower}:books"
    return list(redis_client.smembers(key))

def remove_borrowed_book(borrower: str, title: str):
    key = f"borrower:{borrower}:books"
    redis_client.srem(key, title)

