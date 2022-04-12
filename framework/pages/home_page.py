from framework.elements.button import Button
from framework.pages.base_page import BasePage

from framework.locators.home_page_locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = HomePageLocators.HOME_URL
        self.sign_in_btn = Button(driver, HomePageLocators.SIGN_IN_BTN)

    def load_using_url(self):
        self.driver.get(self.url)
        return self

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def __repr__(self):
        return f'Home page object, class name: {self.__class__.__name__}'
