from pages.product_page import ProductPage
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
