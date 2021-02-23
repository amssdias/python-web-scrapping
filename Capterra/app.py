import json
from selenium import webdriver

from pages.categories_page import CategoriesPage
from locators.categories_page_locator import CategoriesPageLocator

chrome = webdriver.Chrome(executable_path=r'C:\Users\André\Desktop\Programming\chromedriver.exe')
chrome.get('https://www.capterra.com/categories')

page = CategoriesPage(chrome)

categories, letter = [], 64

for i in page.categories:
    x = {
        chr(letter): i.categorie
    }
    letter = letter + 1
    categories.append(x)


chrome.quit()

with open('capterra.json', 'a') as file_:
    json.dump(categories, file_, indent=4)

