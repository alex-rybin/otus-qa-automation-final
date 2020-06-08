import allure
from selenium.webdriver.remote import webelement

from sources.components.base import BaseComponent
from sources.logic.common import Locator


class DropdownMenuLocators:
    BUTTON = Locator('./button')
    MENU = Locator('./div[@class="dropdown-menu"]')
    OPTIONS = Locator('./a[contains(@class, "select-list")]')


class DropdownMenu(BaseComponent):
    _button = None
    _menu = None
    _options = None

    @property
    def button(self) -> webelement:
        if not self._button:
            self._button = self.element.find_element(*DropdownMenuLocators.BUTTON)
        return self._button

    @property
    def menu(self) -> webelement:
        if not self._menu:
            self._menu = self.element.find_element(*DropdownMenuLocators.MENU)
        return self._menu

    @property
    def options(self) -> list:
        if not self._options:
            self._options = self.menu.find_elements(*DropdownMenuLocators.OPTIONS)
        return self._options

    def toggle_menu(self):
        with allure.step('Переключение состояния выпадающего меню'):
            self.button.click()

    def is_open(self) -> bool:
        return self.menu.is_displayed()

    def select(self, value: str):
        with allure.step(f'Выбор опции {value}'):
            if not self.is_open():
                self.toggle_menu()

            for item in self.options:
                label = item.text
                if label == value:
                    item.click()
                    return

        raise ValueError(f'Option "{value}" is not present in menu')
