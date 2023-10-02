from .base_page import BasePage
from .locators import ProductPageLocators
import re
import time


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        BasePage.solve_quiz_and_get_code(self)

        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.NAME_IN_MESSAGE).text
        print(product_name, product_name_in_message)
        assert product_name == product_name_in_message, "Product names are not the same"

        price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        print(price, price_in_message)
        assert price == price_in_message, "Prices are not the same"
