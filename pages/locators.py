from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form button")
    MESSAGE_FORM = (By.CSS_SELECTOR, "#messages")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, "#messages div.alert:nth-child(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, "#messages div.alert:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, "span.btn-group>a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_PRODUCT = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_MESSAGE_FORM = (By.CSS_SELECTOR, "#content_inner>p")

class LoginPageLocators():
    EMAIL_FLD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FLD = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD_FLD = (By.CSS_SELECTOR, "#id_registration-password2")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[name='login_submit']")
    REGISTER_BTN = (By.CSS_SELECTOR, "button[name='registration_submit']")
