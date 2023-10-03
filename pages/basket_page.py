from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS) is True, "Shouldn't be basket items"

    def should_be_your_basket_is_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.YOUR_BASKET_IS_EMPTY)
