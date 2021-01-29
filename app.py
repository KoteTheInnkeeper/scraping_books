import requests

from pages.all_books_page import BooksInPage

page = str(requests.get('http://books.toscrape.com/catalogue/page-1.html').content)


list_of_books = BooksInPage(page)

for book in list_of_books.books:
    print(f"'{book.title}' rated {book.rating.lower()} stars out of five: £%.2f" % book.price)
