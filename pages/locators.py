from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "[class*=register_form]")
    LINK_CONTAINS = "accounts/login/"


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "button[class*=add-to-basket]")
    ADD_TO_CART_MSG = (By.CSS_SELECTOR, "#messages div:nth-child(1) div strong")
    CART_COST_MSG = (By.CSS_SELECTOR, "#messages div:nth-last-child(1) div p strong")
    CART_COST_MINI = (By.CSS_SELECTOR, ".basket-mini")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_COST = (By.CSS_SELECTOR, ".product_main .price_color")
