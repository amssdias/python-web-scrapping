import re

from locators.book_locators import BookLocators

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

    def __repr__(self):
        return f"<Book {self.name}, £{self.price} ({self.rating} stars)"

    @property
    def name(self):
        return self.parent.select_one(BookLocators.NAME_LOCATOR).attrs['title']
    
    @property
    def link(self):
        return self.parent.select_one(BookLocators.LINK_LOCATOR).attrs['href']

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
        # stars = filter(lambda x: x != 'star-rating', star_class)
        stars = [r for r in star_class if r != 'star-rating']
        # Get method None if not found
        rating_number = BookParser.RATINGS.get(stars[0])
        return rating_number