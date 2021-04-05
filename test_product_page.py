from pages.product_page import ProductPage
import pytest


base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
promo_links = [base_link + '/?promo=offer' + str(n) if n != 7
               else pytest.param(base_link + '/?promo=offer' + str(n), marks=pytest.mark.xfail(reason="Improper bold"))
               for n in range(10)]


@pytest.mark.parametrize('link', promo_links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_item_name_in_add_to_cart_message()
    page.should_be_correct_cart_sum()
