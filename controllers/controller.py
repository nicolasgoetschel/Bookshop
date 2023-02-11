from flask import render_template, request, redirect
from app import app
from models.book import *
from models.book_list import book_list, add_new_book, delete_book

@app.route('/')
def index():
    return render_template("index.html", book_list = book_list)


@app.route('/books')
def display_books():
    return render_template("display_books", book_list = book_list)

@app.route('/books/<display_books>')
def book_detail(display_stock):
    chosen_book = book_list [int(display_books)]
    return render_template ('single_book.html', book = chosen_book, book_list = book_list)

@app.route('/books/add')
def new_book():
    return render_template('add_book.html')

@app.route('/booksabc', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    description = request.form['description']
    if request.form.get('available'):
        availability = True
    else:
        availability = False 
    new_book = Book (title, author, genre, description, availability)
    add_new_book(new_book)
    return redirect("/booksabcd")

@app.route('/books/delete/', methods =['POST'])
def delete():
    index_to_delete = int(request.form["delete"])
    delete_book(index_to_delete)
    return redirect("/books")