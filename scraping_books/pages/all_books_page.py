from bs4 import BeautifulSoup

from locators.all_books_page import AllBooksPageLocators
from parsers.book_parser import BookParser

class AllBooksPage:
    def __init__(self, soup):
        self.soup = BeautifulSoup(soup, 'html.parser')

    @property
    def books(self):
        books = AllBooksPageLocators.BOOKS
        all_books = self.soup.select(books)
        return [BookParser(e) for e in all_books]