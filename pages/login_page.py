from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.enter_repeat_password(password)
        self.click_register_button()

    
    def enter_email(self, email):
        email_fld = self.browser.find_element(*LoginPageLocators.EMAIL_FLD)
        email_fld.send_keys(email)
    
    def enter_password(self, password):
        password_fld = self.browser.find_element(*LoginPageLocators.PASSWORD_FLD)
        password_fld.send_keys(password)

    def enter_repeat_password(self, password):
        rep_password_fld = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_FLD)
        rep_password_fld.send_keys(password)
    
    def click_login_button(self):
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_btn.click()
    
    def click_register_button(self):
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()

