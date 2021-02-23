from parsers.categories_parser import CategorieParser
from locators.categories_page_locator import CategoriesPageLocator

class CategoriesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def categories(self):
        categories_list = self.browser.find_elements_by_css_selector(CategoriesPageLocator.CATEGORIES)
        return [CategorieParser(e) for e in categories_list]