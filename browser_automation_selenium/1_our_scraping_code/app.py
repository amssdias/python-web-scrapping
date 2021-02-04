from selenium import webdriver

from pages.quotes_page import QuotesPage, InvalidTagForAuthorError

try:
    author = input("Enter the author you'd like quotes from: ")
    tag = input('Enter your tag: ')

    chrome = webdriver.Chrome(executable_path=r'C:\Users\André\Desktop\Programming\chromedriver.exe')
    chrome.get('http://quotes.toscrape.com/search.aspx')
    page = QuotesPage(chrome)


    print(page.search_for_quotes(author,tag))

except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An unknown error occurred. Please try again.")




# page.select_author(author)
# tags = page.get_available_tags()
# print('Select one of these tags: [{}]'.format(" | ".join(tags)))
# page.select_tag(selected_tag)
# page.search_button.click()

# print(page.quotes)