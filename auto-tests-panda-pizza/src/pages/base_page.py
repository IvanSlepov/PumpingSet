from src.testData.test_pages import TestPages
from src.pages.locators.base_page_locators import BasePageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    """Base page class."""

    def __init__(self, driver: Remote):
        """Initialize main class.

        :param driver: Remote.
        """

        self._driver: Remote = driver
        self.base_url: str = TestPages.MAIN_PAGE

    def find_element(self, locator: tuple[str, str], time=20) -> WebElement:
        """Method that finds elements on page.
        :param:
        :return: WebElement
        """
        return WebDriverWait(self._driver, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_elements(self, locator: tuple[str, str], time=10) -> list[WebElement]:
        """Method that finds elements on page.
        :param: string
        :return: Tuple[WebElements]
        """
        return WebDriverWait(self._driver, time).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

    def go_to_site(self) -> None:
        """Method that goes to the main page.
        :return: None
        """
        self._driver.get(self.base_url)

    def close_blocking_message(self, time=10) -> None:
        """Method that closes the message,
        that appears when the page is opened
        :return: None"""
        WebDriverWait(self._driver, time).until(EC.presence_of_element_located
        (
            BasePageLocators.LOCATOR_BLOCKING_MESSAGE),
            message=f"Can't find element by locator {BasePageLocators.LOCATOR_BLOCKING_MESSAGE}"
        ).click()

# if __name__ == '__main__':
#     browser = Firefox()
#     browser.maximize_window()
#     panda_pizza = BasePage(browser)
#     panda_pizza.go_to_site()
