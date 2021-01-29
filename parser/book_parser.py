import re

from locators.books_locator import BookLocator, AttributesReg


class BookParser:
    """
        Given an specific 'book' item in the page, this would make an object with the desired caracteristics.
    """
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"Book '{self.title}', rated {self.rating.lower()}"

    @property
    def title(self):
        locator = BookLocator.TITLE
        return self.parent.select_one(locator).attrs['title']

    @property
    def rating(self):
        locator = BookLocator.RATING
        classes = self.parent.select_one(locator).attrs['class']
        star_rating = [e for e in classes if e != 'star-rating']
        return star_rating[0]

    @property
    def price(self):
        locator = BookLocator.PRICE
        price_string = str(self.parent.select_one(locator).string)
        regex = AttributesReg.PRICE_NUMBER
        matches = re.findall(regex, price_string)
        return float(matches[1])




