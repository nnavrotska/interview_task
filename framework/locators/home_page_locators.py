from selenium.webdriver.common.by import By
from framework import config

class HomePageLocators:
    HOME_URL = config.SITE
    SIGN_IN_BTN = (By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')

    def __repr__(self):
        return f'Home Page Locators object, class name: {self.__class__.__name__}'
