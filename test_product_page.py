from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_product_to_basket()          # выполняем метод страницы — переходим на страницу логина
    page.solve_quiz_and_get_code()
    page.should_be_message_form()
    page.should_be_product_name()
    page.should_be_product_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    page.open()                      # открываем страницу
    page.add_product_to_basket()
    page.should_not_be_success_message() #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
 

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    page.open()                      # открываем страницу
    page.should_not_be_success_message()  #Проверяем, что нет сообщения об успехе с помощью is_not_element_present
 
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    page.open()                      # открываем страницу
    page.add_product_to_basket()
    time.sleep(1)
    page.should_not_disapear_message() #Проверяем, что нет сообщения об успехе с помощью is_disappeared

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_pg = BasketPage(browser, browser.current_url)
    basket_pg.should_not_be_products()
    basket_pg.should_be_message_empty_basket()



class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "KDNVdk3s12"
        page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/") 
        page.open()
        page.add_product_to_basket()
        page.should_be_message_form()
        page.should_be_product_name()
        page.should_be_product_price()