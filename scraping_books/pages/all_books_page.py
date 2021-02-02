import re
from bs4 import BeautifulSoup

from locators.all_books_page import AllBooksPageLocators
from parsers.book_parser import BookParser

class AllBooksPage:
    def __init__(self, soup):
        self.soup = BeautifulSoup(soup, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]

    @property
    def page_count(self):
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        return pages