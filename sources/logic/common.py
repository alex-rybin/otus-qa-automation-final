from typing import NamedTuple

from selenium.webdriver.common.by import By


class Locator(NamedTuple):
    path: str
    path_type: str = By.XPATH

    def format(self, **kwargs):
        return self.path_type, self.path.format(**kwargs)

    def __iter__(self):
        yield self.path_type
        yield self.path
