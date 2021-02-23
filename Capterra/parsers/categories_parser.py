from locators.categories_locator import CategoriesLocator

class CategorieParser:
    def __init__(self, parent):
        self.parent = parent
    
    def __repr__(self):
        return f"<Categorie: {self.parent}"
    
    @property
    def categorie(self):
        locator = CategoriesLocator.CATEGORY
        all_categories = self.parent.find_elements_by_css_selector(locator)
        return [e.text for e in all_categories]