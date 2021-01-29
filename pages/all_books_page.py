import logging, re, requests

from bs4 import BeautifulSoup
from locators.in_page_parents import PageReg, PageLocator, BookPageLocator
from parser.book_parser import BookParser


class BooksInPage:
    def __init__(self, url: str):
        page_content = str(requests.get(url).content)
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self) -> list:
        locator = BookPageLocator.BOOK
        books_tags = self.soup.select(locator)
        return [BookParser(e) for e in books_tags]


class PageGenerator:
    def __init__(self, url: str):
        self.soup_for_page = BeautifulSoup(str(requests.get(url).content), 'html.parser')
        self.number = 1
        self.url = url

    @property
    def last(self) -> int:
        locator = PageLocator.PAGER
        page_tag = self.soup_for_page.select_one(locator).string
        regex = PageReg.TOTAL_PAGES
        matches = re.search(regex, page_tag)
        last_page = int(matches.group(1))
        return last_page

    def __next__(self) -> str:
        if self.number <= self.last:
            current = self.number
            self.number += 1
            return self.divided_page[0] + str(current) + self.divided_page[1]
        else:
            raise StopIteration()

    @property
    def divided_page(self) -> list:
        regex = PageReg.URL_DIVIDER
        matches = re.findall(regex, self.url)
        return matches

    def __iter__(self):
        return self




