from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Temporary storage for books and reviews
books_db = {}
reviews_db = {}


class Book(BaseModel):
    title: str
    author: str
    publication_year: int


class Review(BaseModel):
    book_id: int
    text: str
    rating: int


# Endpoint to add a new book
@app.post("/books/")
async def add_book(book: Book):
    book_id = len(books_db) + 1
    books_db[book_id] = book
    return {"message": "Book added successfully", "book_id": book_id}


# Endpoint to submit a review for a book
@app.post("/books/{book_id}/reviews/")
async def add_review(book_id: int, review: Review):
    if book_id not in books_db:
        return {"error": "Book not found"}
    reviews_db.setdefault(book_id, []).append(review)
    return {"message": "Review added successfully"}


# Endpoint to retrieve all books with optional filters
@app.get("/books/")
async def get_books(author: str = None, publication_year: int = None):
    filtered_books = []
    for book_id, book in books_db.items():
        if (not author or author == book.author) and (not publication_year or publication_year == book.publication_year):
            filtered_books.append({"book_id": book_id, "title": book.title, "author": book.author, "publication_year": book.publication_year})
    return filtered_books


# Endpoint to retrieve all reviews for a specific book
@app.get("/books/{book_id}/reviews/")
async def get_reviews(book_id: int):
    if book_id not in books_db:
        return {"error": "Book not found"}
    if book_id not in reviews_db:
        return {"message": "No reviews found for this book"}
    return reviews_db[book_id]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
