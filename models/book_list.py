from models.book import Book
import datetime


book_1 = Book("Tristram Shandy", "Laurence Sterne", "Novel", "ABC", True)
book_2 = Book("The Brothers Karamazov", "Fyodor Dostoyevsky", "Philosophical Novel", "DEF", True)
book_3 = Book("Midnight's Children", "Salman Rushdie", "Magic Realism", "GHI", True)
book_4 = Book("The Grapes of Wrath", "John Steinbeck", "Novel", "JKL", False)
book_5 = Book("The Trial", "Franz Kafka", "Philosophical Fiction", "MNO", False)

book_list = [book_1, book_2, book_3, book_4, book_5]

def add_new_book(book):
    book_list.append(book)

def delete_book(index):
    book_list.pop(index)
