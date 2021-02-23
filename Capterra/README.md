# CAPTERRA


I have seen a job offer online to scrape all categories from this website so decided to do it myself just for practice and fun.
All categories are being saved in a json file called __*capterra.json*__

Website we will scrape - [capterra](https://www.capterra.com/categories)


## Requirements

- Selenium library
- A webdriver

### Selenium

Install `selenium` using PyCharm's preferences panel or in your virtual environment.

### Webdriver

(Chrome Driver)[https://chromedriver.chromium.org/]
Make sure to download the version for your browser (e.g. v74 if you're using Chrome v74).

Place the de-compressed executable, chromedriver, into a folder. Remember the folder's path, as you'll need it after.



## Structure

```
├───locators
├───pages
└───parsers
```

### Locators

Have 2 files each with a class with constant variables showing where we locate the groups of categories to select each categorie.

```python
class CategoriesPageLocator:
    CATEGORIES = "div.browse div.cell.one-whole"
```

```python
class CategoriesLocator:
    CATEGORY = 'ol li a'
```

### Parsers

A file with a class to find out each categorie. We get a list and we access them as propertys.

```python
class CategorieParser:
    def __init__(self, parent):
        self.parent = parent
    
    @property
    def categorie(self):
        locator = CategoriesLocator.CATEGORY
        all_categories = self.parent.find_elements_by_css_selector(locator)
        return [e.text for e in all_categories]
```

### Pages

In here we create our main class and we gave a method to get a list of a group of categories.

```python
class CategoriesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def categories(self):
        categories_list = self.browser.find_elements_by_css_selector(CategoriesPageLocator.CATEGORIES)
        return [CategorieParser(e) for e in categories_list]
```