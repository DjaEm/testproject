from .base_page import BasePage
from .locators import ProductPageLocators
import re
import time


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        BasePage.solve_quiz_and_get_code(self)
        time.sleep(5)
