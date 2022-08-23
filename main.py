from fastapi import FastAPI
from models import Book, Author
from typing import List


app = FastAPI(title="Bookstore API", description="This is a bookstore API")

book = [Book(name="The Art of Computer Programming", author=Author(name="Donald Knuth", age=70), genre="Computer Science", released=True, price=39.99), 
        Book(name="The C Programming Language", author=Author(name="Dennis Ritchie", age=70), genre="Computer Science", released=True, price=39.99), 
        Book(name="The Little Book on CoffeeScript", author=Author(name="Alex MacCaw", age=70), genre="Computer Science", released=True, price=39.99)]

authors = [Author(name="Donald Knuth", age=70), Author(name="Dennis Ritchie", age=70), Author(name="Alex MacCaw", age=70)]

@app.get("/")
async def root():
    return {"greeting": "Welcome to the bookstore API"}

@app.get("/books")
async def get_books():
    return book

@app.get("/book/{book_id}")
async def get_book(book_id: int):
    try:
        return book[book_id]
    except IndexError:
        return {"message": "Book not found"}, 404

@app.post("/book")
async def add_book(book: Book):
    book.append(book)
    return book

@app.put("/book/{book_id}")
async def update_book(book_id: int, book: Book):
    try:
        book[book_id] = book
        return book
    except IndexError:
        return {"message": "Book not found"}, 404

@app.delete("/book/{book_id}")
async def delete_book(book_id: int):
    try:
        book.pop(book_id)
        return book
    except IndexError:
        return {"message": "Book not found"}, 404\

@app.put("/book/{book_id}/release")
async def release_book(book_id: int):
    try:
        book[book_id].released = True
        return book[book_id]
    except IndexError:
        return {"message": "Book not found"}, 404

@app.get("/authors")
async def get_authors():
    return [author.name for author in book]

@app.put("/authors")
async def add_authors(authors: List[Author]):
    for author in authors:
        book.append(author)
    return book

@app.put("/authors/{author_id}")
async def update_authors(author_id: int, author: Author):
    try:
        book[author_id] = author
        return book
    except IndexError:
        return {"message": "Author not found"}, 404

