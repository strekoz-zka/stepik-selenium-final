from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM)

    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MSG)
