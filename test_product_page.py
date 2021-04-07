import time

from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
import pytest


base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
promo_links = [base_link + '/?promo=offer' + str(n) if n != 7
               else pytest.param(base_link + '/?promo=offer' + str(n), marks=pytest.mark.xfail(reason="Improper bold"))
               for n in range(10)]


@pytest.mark.skip(reason='for testing reasons')
@pytest.mark.parametrize('link', promo_links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_item_name_in_add_to_cart_message()
    page.should_be_correct_cart_sum()


@pytest.mark.skip(reason="Wrong test case")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="ticket in process")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, base_link)
    page.open()
    page.add_to_cart()
    page.should_success_message_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.guest_opens_basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_empty()
    basket.should_be_empty_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        login_page = LoginPage(browser, login_link)
        login_page.open()
        random_element = str(time.time())
        email = random_element + '@fake.org'
        password = "passw0rd" + random_element
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, base_link)
        page.open()
        page.should_not_be_success_message()

    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, base_link)
        page.open()
        page.add_to_cart()
        page.should_be_item_name_in_add_to_cart_message()
        page.should_be_correct_cart_sum()
