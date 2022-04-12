from framework.elements.base_element import BaseElement


class Button(BaseElement):
    def click(self):
        self.web_element.click()

    def get_text(self):
        return self.web_element.get_attribute('text')

    def __repr__(self):
        return f'Button element object, class name: {self.__class__.__name__}'
