from pages.main_page import MainPage
from pages.locators import ProductPageLocators


class ProductPage(MainPage):
    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def should_be_item_name_in_add_to_cart_message(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        add_to_cart_msg = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_MSG).text
        assert add_to_cart_msg == item_name, 'Add to cart message does not contain the correct item name'

    def should_be_correct_cart_sum(self):
        item_cost = self.browser.find_element(*ProductPageLocators.ITEM_COST).text
        cart_cost_msg = self.browser.find_element(*ProductPageLocators.CART_COST_MSG).text
        cart_cost_mini = self.browser.find_element(*ProductPageLocators.CART_COST_MINI).text
        assert cart_cost_msg == item_cost, 'Add to cart message does not contain correct item cost'
        assert item_cost in cart_cost_mini, 'Cart cost does not contain correct sum total'
