from typing import Union

from framework.elements.base_element import BaseElement


class Input(BaseElement):
    @property
    def text(self) -> str:
        return self.web_element.get_attribute("value")

    @text.setter
    def text(self, value: Union[str, int]) -> None:
        self.web_element.clear()
        self.web_element.send_keys(value)
