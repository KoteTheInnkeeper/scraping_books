from pages.all_books_page import BooksInPage, PageGenerator, Bookshelf

# This is the first page of the website when asked to show by pages
initial_page = 'http://books.toscrape.com/catalogue/page-1.html'

# This is an iterable generator with each page, accounting from the '1' to the 'last one'. The 'last page' number
# is also scraped from the page.
page_range = PageGenerator(initial_page)

# Lets generate a Bookshelf object for holding the books in page.
web_bookshelf = Bookshelf()


for page in page_range:
    books_in_this_page = BooksInPage(page)
    for book in books_in_this_page.books:
        web_bookshelf + book

input("Books scraped!. Press enter to show them!\n")

print(web_bookshelf)
