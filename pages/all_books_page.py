import logging, re

from bs4 import BeautifulSoup
from locators.in_page_parents import PageReg, PageLocator, BookPageLocator
from parser.book_parser import BookParser


class BooksInPage:
    def __init__(self, page: str):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self) -> list:
        locator = BookPageLocator.BOOK
        books_tags = self.soup.select(locator)
        return [BookParser(e) for e in books_tags]

