from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException


class BaseElement:
    def __init__(self, driver, locator=None, description: str = "", parent_element=None):
        self.driver = driver
        self.locator = locator
        self.description = f"{description} | {self.locator}" if description else f"element with locator {self.locator}"
        self.parent_element = parent_element

    @property
    def web_element(self) -> WebElement:
        if self.parent_element:
            return self.parent_element.web_element.find_element(*self.locator)
        return self.driver.find_element(*self.locator)

    @property
    def text(self) -> str:
        return self.web_element.text

    def click(self) -> None:
        self.web_element.click()

    def is_visible(self) -> bool:
        try:
            return self.web_element.is_displayed()
        except NoSuchElementException:
            return False

    def __repr__(self):
        return f'Base Element object, class name: {self.__class__.__name__}'
