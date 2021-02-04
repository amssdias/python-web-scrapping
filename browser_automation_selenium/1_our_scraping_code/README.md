# Browser automation with Selenium

Now we're launching a browser instead of requesting the page with Python. We will be controlling the browser, instead of just getting HTML.

The browser will work like a normal browser: it will run JavaScript, it will have cookies, etc...

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

Have 2 files each with a class with constant variables showing where we locate the dropdown to select the author, the tag, the button to search so we then can find the quote, the author and the tag.

```python
class QuotesPageLocators:
    QUOTE = "div.quote"
    AUTHOR_DROPDOWN = "select#author"
    TAG_DROPDOWN = "select#tag"
    TAG_DROPDOWN_VALUE_OPTION = 'select#tag option[value]'
    SEARCH_BUTTON = "input[name='submit_button']"
```

```python
class QuoteLocators:
    CONTENT_LOCATOR = 'span.content'
    AUTHOR_LOCATOR = 'span.author'
    TAGS_LOCATOR = 'span.tag'
```

### Parsers

A file with a class to find out the data about the quote (quote content, author, tags). This class have three methods: **content**, **author**, **tags**. We can access them as propertys.

```python
class QuoteParser:
    def __init__(self, parent):
        self.parent = parent

    @property
    def content(self):
        locator = QuoteLocators.CONTENT_LOCATOR
        return self.parent.find_element_by_css_selector(locator).text
```

### Pages

In here we create our main class and we gave few methods so there's few different ways to search for the data. Our main method using in the program is the `search_for_quotes` as we want to abstract our logic from the main page so we don't have to call too many methods. 

```python
class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        return [
            QuoteParser(e) 
            for e in self.browser.find_elements_by_css_selector(
                QuotesPageLocators.QUOTE
            )
        ]

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(QuotesPageLocators.AUTHOR_DROPDOWN)
        return Select(element)
    
    @property
    def tags_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(QuotesPageLocators.TAG_DROPDOWN)
        return Select(element)
    
    @property
    def search_button(self):
        return self.browser.find_element_by_css_selector(QuotesPageLocators.SEARCH_BUTTON)

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tags_dropdown.options]

    def select_tag(self, tag_name: str):
        self.tags_dropdown.select_by_visible_text(tag_name)

    def search_for_quotes(self, author_name: str, tag_name: str) -> List[QuoteParser]:
        self.select_author(author_name)

        WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, QuotesPageLocators.TAG_DROPDOWN_VALUE_OPTION)
            )
        )

        try:
            self.select_tag(tag_name)
        except NoSuchElementException:
            raise InvalidTagForAuthorError(
                f"Author '{author_name}' does not have any quotes tagged with '{tag_name}'."
        )
        self.search_button.click()
        return self.quotes
```