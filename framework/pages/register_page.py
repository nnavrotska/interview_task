from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from framework import config
from framework.elements.button import Button
from framework.elements.base_element import BaseElement
from framework.elements.input import Input
from framework.locators.register_page_locators import RegisterPageLocators
from framework.pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = RegisterPageLocators.REGISTER_URL
        self.create_an_account_btn = Button(driver, RegisterPageLocators.CREATE_AN_ACCOUNT_BTN)
        self.user_email_input = Input(driver, RegisterPageLocators.USER_EMAIL)
        self.alert_warning = BaseElement(driver, RegisterPageLocators.INVALID_EMAIL_ALERT)

    def load_using_url(self):
        self.driver.get(self.url)
        return self

    def get_title(self):
        return self.driver.title

    def register_user(self, user_email: str):
        self.user_email_input.text = user_email
        self.create_an_account_btn.click()

    def get_current_url(self):
        return self.driver.current_url

    def get_warning_message(self):
        wait = WebDriverWait(self.driver, config.IMPLICIT_WAIT)
        wait.until(ec.presence_of_element_located(RegisterPageLocators.INVALID_EMAIL_ALERT))
        self.alert_warning.is_visible()
        return self.alert_warning.text

    def __repr__(self):
        return f'Register page object, class name: {self.__class__.__name__}'
