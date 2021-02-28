from .pages.main_page import MainPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/ru/"

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_pg = BasketPage(browser, browser.current_url)
    basket_pg.should_not_be_products()
    basket_pg.should_be_message_empty_basket()