from flask import render_template, request, redirect
from app import app
from models.book_list import book_list, add_new_book, delete_book
from models.book import Book

@app.route('/')
def index():
    return render_template('index.html',title='Home', book_list=book_list)

@app.route('/books')
def show_all_books():
    return render_template('books.html', book_list = book_list)

@app.route('/books/new')
def new_book():
  return render_template("add_book.html")

@app.route('/books/add', methods=['POST'])
def add_book():
  title = request.form['title']
  author = request.form['author']
  genre = request.form['genre']
  if request.form.get("available"):
    availability = True
  else:
    availability = False
  new_book = Book (title, author, genre, availability)
  add_new_book(new_book)
  return redirect("/books")

@app.route('/books/<show_all_books>')
def book_information(show_all_books):
    selected_book = book_list [int(show_all_books)]
    return render_template ('single_book.html', book = selected_book, book_list = book_list)

@app.route('/books/delete/', methods =['POST'])
def delete():
    index_to_delete = int(request.form["delete"])
    delete_book(index_to_delete)
    return redirect("/books")

