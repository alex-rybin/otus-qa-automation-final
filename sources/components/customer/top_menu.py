import allure
from selenium.webdriver import ActionChains

from sources.components.base import BaseComponent
from sources.logic.common import Locator


class TopMenuLocators:
    MENU_OPTION = Locator('./li/a[text()[contains(., "{text}")]]')
    SUBMENU = Locator('./following-sibling::div[1]/ul[@class="top-menu"]')


class TopMenu(BaseComponent):
    def click_menu_element(self, *menu_path: str):
        message = ' > '.join(menu_path)
        with allure.step(f'Переход в верхнем меню в раздел {message}'):
            parent = self.element

            for element in menu_path[:-1]:
                menu_item = parent.find_element(*TopMenuLocators.MENU_OPTION.format(text=element))
                ActionChains(self.browser).move_to_element(menu_item).perform()
                parent = menu_item.find_element(*TopMenuLocators.SUBMENU)

            parent.find_element(*TopMenuLocators.MENU_OPTION.format(text=menu_path[-1])).click()
