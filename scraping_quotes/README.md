# Scraping quotes

In this repository I'm scrapping quotes, author and tags from a website. Testing my skills, using a very well structured code within the folders.

Website used to scrape: `http://quotes.toscrape.com`

## Pre requisites

 * [Python](https://www.python.org/downloads/) - 3.8.4 or up

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

Have 2 files each with a class with constant variables showing where we locate each quote, and from each quote where we locate each author, quote and tags.

```python
class QuotesPageLocators:
    QUOTE = 'div.quote'
```

```python
class QuoteLocators:
    AUTHOR = 'small.author'
    CONTENT = 'span.text'
    TAGS = 'div.tags a.tag'
```

### Parsers

A file with a class to find out the data about the quote (quote content, author, tags). This class have three methods: **content**, **author**, **tags**. We can access them as propertys.

```python
class QuoteParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.select_one(locator).string
```

### Pages

In here we create our main class and we only give one method which will give us each quote as an object so we can access them as objects and get the author, quote and tags from each single object.

```python
class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.soup.select(locator)
        return [QuoteParser(e) for e in quote_tags]
```