from pages.all_books_page import BooksInPage, PageGenerator

# This is the first page of the website when asked to show by pages
initial_page = 'http://books.toscrape.com/catalogue/page-1.html'

# This is an iterable generator with each page, accounting from the '1' to the 'last one'. The 'last page' number
# is also scraped from the page.
page_range = PageGenerator(initial_page)

for x, page in enumerate(page_range, start=1):
    books_in_this_page = BooksInPage(page)
    for i, book in enumerate(books_in_this_page.books, start=1):
        print(f"{i}) '{book.title}' rated {book.rating.lower()} stars out of five: £{book.price}")
    print(f"Page {x} of {page_range.last}")
# books = BooksInPage(page)

