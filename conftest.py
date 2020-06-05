import logging

import pytest
from envparse import env
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait

from sources.logic.common import Locator

env.read_envfile('.env.local')

BASE_URL = f'http://{env.str("PRESTASHOP_HOST")}'
BROWSER_CHOICES = ['firefox', 'chrome', 'opera']
HEADER = Locator('//img[@alt="PrestaShop"]')


class EventListener(AbstractEventListener):
    def __init__(self, logger):
        super().__init__()
        self.logger = logger

    def after_change_value_of(self, element, driver):
        self.logger.info(f'Changed value of {element}')

    def after_click(self, element, driver):
        self.logger.info(f'Clicked on {element}')

    def after_close(self, driver):
        self.logger.info(f'Closed window of {driver}')

    def after_execute_script(self, script, driver):
        self.logger.info(f'Executed script: {script}')

    def after_find(self, by, value, driver):
        self.logger.info(f'Searched {value} by {by}')

    def after_navigate_back(self, driver):
        self.logger.info('Navigated back')

    def after_navigate_forward(self, driver):
        self.logger.info('Navigated forward')

    def after_navigate_to(self, url, driver):
        self.logger.info(f'Opened URL: {url}')

    def after_quit(self, driver):
        self.logger.info('Browser quit')

    def before_change_value_of(self, element, driver):
        self.logger.info(f'Changing value of {element}')

    def before_click(self, element, driver):
        self.logger.info(f'Clicking on {element}')

    def before_close(self, driver):
        self.logger.info('Closing window')

    def before_execute_script(self, script, driver):
        self.logger.info(f'Executing script: {script}')

    def before_find(self, by, value, driver):
        self.logger.info(f'Searching {value} by {by}')

    def before_navigate_back(self, driver):
        self.logger.info('Navigating back')

    def before_navigate_forward(self, driver):
        self.logger.info('Navigating forward')

    def before_navigate_to(self, url, driver):
        self.logger.info(f'Opening URL: {url}')

    def before_quit(self, driver):
        self.logger.info('Quitting browser')

    def on_exception(self, exception, driver):
        self.logger.warning(f'Exception thrown: {exception}')


def pytest_addoption(parser):
    parser.addoption(
        '-B',
        '--browser',
        default=BROWSER_CHOICES[0],
        choices=BROWSER_CHOICES,
        help=(
            f'Browser to use in tests. '
            f'Can be one of: {", ".join(BROWSER_CHOICES)}. Default: {BROWSER_CHOICES[0]}'
        ),
    )


@pytest.fixture(scope='session')
def logger():
    logging.basicConfig(
        format='%(asctime)s %(name)s [%(levelname)s]: %(message)s', level=logging.INFO, force=True
    )
    return logging.getLogger('Fixture')


@pytest.fixture
def browser(logger, request):
    selected_browser = request.config.getoption('--browser')

    browser = EventFiringWebDriver(
        webdriver.Remote(
            command_executor=f'http://{env.str("SELENOID_HOST")}:4444/wd/hub',
            desired_capabilities={
                'browserName': selected_browser,
                'acceptInsecureCerts': True,
            },
        ),
        EventListener(logging.getLogger('Browser')),
    )

    request.addfinalizer(browser.quit)

    browser.get(f'http://{env.str("PRESTASHOP_HOST")}')
    # Ожидание на случай первоначальной установки
    WebDriverWait(browser, 100).until(EC.visibility_of_element_located(HEADER))

    return browser
