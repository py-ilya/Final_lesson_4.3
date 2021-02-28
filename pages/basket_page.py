from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT), \
        "Product is presented, but should not be"
    
    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE_FORM), \
        "Message Form is not presented"