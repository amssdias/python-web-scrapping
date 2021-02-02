import re
import logging

from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')

class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        logger.debug(f"New book parser created from `{parent}`")
        self.parent = parent

    def __repr__(self):
        return f"<Book {self.name}, £{self.price} ({self.rating} stars)"

    @property
    def name(self):
        logger.debug('Finding book name...')
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        logger.debug(f'Found book name, `{item_name}`.')
        return item_name
    
    @property
    def link(self):
        logger.debug('Finding book link...')
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator).attrs['href']
        logger.debug(f'Found book link, `{item_link}`.')
        return item_link

    @property
    def price(self):
        logger.debug('Finding book price...')
        price = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(price).string

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        float_price = float(matcher.group(1))
        logger.debug(f'Found book price, `{float_price}`.')
        return float_price

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        stars = self.parent.select_one(BookLocators.RATING_LOCATOR)
        star_class = stars.attrs['class']
        # stars = filter(lambda x: x != 'star-rating', star_class)
        stars = [r for r in star_class if r != 'star-rating']
        # Get method None if not found
        rating_number = BookParser.RATINGS.get(stars[0])
        logger.debug(f'Found book rating, `{rating_number}`.')
        return rating_number