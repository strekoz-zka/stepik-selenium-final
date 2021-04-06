from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_ICON = (By.CSS_SELECTOR, ".basket-mini .btn-group>a")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    


class BasketPageLocators:
    BASKET_ITEM = (By.CSS_SELECTOR, "#content_inner .basket-items")
    EMPTY_BASKET_MSG = (By.CSS_SELECTOR, "#content_inner>p")


class MainPageLocators:
    pass


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
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div")
