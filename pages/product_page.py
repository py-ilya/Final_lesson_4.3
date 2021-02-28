from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_button.click()
    
    def should_be_message_form(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_FORM), "Message Form is not presented"

    def should_be_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BASKET).text
        assert product_name == product_name_basket, "Product name is not equal"
    
    def should_be_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        prosuct_price_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_BASKET).text
        assert product_price == prosuct_price_basket, "Product price is not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
    
    def should_not_disapear_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is disapear, but should not be"
