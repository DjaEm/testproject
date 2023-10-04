from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.remote.webdriver import WebDriver
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Should be login in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Should be login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Should be register form"

    def register_new_user(self, password="some_password"):
        email = str(time.time()) + "@fakemail.org"
        self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT).click()
