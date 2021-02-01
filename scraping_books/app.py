import requests
from pages.all_books_page import AllBooksPage

page_content = requests.get('https://books.toscrape.com/').content

book_page = AllBooksPage(page_content)

for book in book_page.books:
    print(book)
