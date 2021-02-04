# Scraping Books

In this repository I'm scrapping name, link, price and ratings from a book from a website. Testing my skills, using a very well structured code within the folders.

Website used to scrape: [books.toscrape.com/](https://books.toscrape.com/)

 ### Libraries

 * Requests
 * Beautifulsoup4

  #### To install:
  After installing **Python** open your terminal window and type:
  - ```pip install requests```
  - ```pip install beautifulsoup4```


## Run

Download the folder, open your terminal window on the project folder and type:
```
python app.py
```

You will get a list of all quotes from the website.


## Structure

```
├───locators
├───pages
└───parsers
```

### Locators

Have 2 files each with a class with constant variables showing where we locate each book, and from each book where we locate each title, link, price and rating.

```python
class AllBooksPageLocators:
    BOOKS = 'div.page_inner section li.col-xs-6.col-sm-4.col-md-3.col-lg-3'
```

```python
class BookLocators:
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'
```

### Parsers

A file with a class to find out the data about the book (name, link, price and rating). This class have four methods: **name**, **link**, **price** and **rating**. We can access them as propertys.

```python
class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    @property
    def name(self):
        return self.parent.select_one(BookLocators.NAME_LOCATOR).attrs['title']
    
    @property
    def link(self):
        return self.parent.select_one(BookLocators.NAME_LOCATOR).attrs['href']

    @property
    def price(self):
        price = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(price).string

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        return float(matcher.group(1))

    @property
    def rating(self):
        stars = self.parent.select_one(BookLocators.RATING_LOCATOR)
        star_class = stars.attrs['class']
        stars = [r for r in star_class if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(stars[0])
        return rating_number
```

### Pages

In here we create our main class and we only give one method which will give us each book as an object so we can access them as objects and get the name, link, price and rating from each single object.

```python
class AllBooksPage:
    def __init__(self, soup):
        self.soup = BeautifulSoup(soup, 'html.parser')

    @property
    def books(self):
        books = AllBooksPageLocators.BOOKS
        all_books = self.soup.select(books)
        return [BookParser(e) for e in all_books]
```