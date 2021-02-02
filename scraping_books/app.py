import requests
from pages.all_books_page import AllBooksPage

books = []

for page_num in range(1, 50):
    url = f'https://books.toscrape.com/catalogue/page-{page_num}.html'
    page_content = requests.get(url).content
    page = AllBooksPage(page_content)
    books.append(page.books)

print(books)