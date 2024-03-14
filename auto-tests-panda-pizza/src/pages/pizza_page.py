import src.pages.locators as Locators
import src.testData as TestData

from src.pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Remote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PizzaPage(BasePage):
    def __init__(self, driver: Remote):
        """Initialize driver and objects to works with 'Pizza' page.

        :param driver: Remote
        """
        super().__init__(driver)
        self.product_list: list = []

    def go_to_pizza_page(self) -> None:
        """Method thar proceeds to the Pizza page.

        :return:None
        """
        self._driver.get(TestData.TestPages.PRODUCT_PAGE)

    def generate_product_list(self) -> list:
        """Fills product_list with PropertyOfProduct class instances.
        This method must be called before you start working with product methods.

        :return: list of PropertyOfProduct class instances
        """
        products: list = self._driver.find_elements(*Locators.PizzaPageLocators.LOCATOR_PIZZAS)
        for product in products:
            self.product_list.append(PropertyOfProduct(product))
        return self.product_list

    def get_products_name_list(self) -> list:
        """Method that returns list with name of product.

        :return: list
        """
        product_names_list: list = []
        for product in self.product_list:
            product_names_list.append(product.get_name())
        return product_names_list

    def add_product_to_shopping_cart(self, product_name: str) -> None:
        """Method that adds appointed product to the cart.

         :param: string
         :return: None
         """
        for product in self.product_list:
            if product.get_name() == product_name:
                product.click_add_to_cart()

    def check_items_in_cart(self) -> str:
        """Method that returns the number of items in cart.

        :return: string
        """
        message = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located(Locators.CheckoutLocators.LOCATOR_NUMBER_OF_ITEMS_IN_CART)
        )
        return message.text


class PropertyOfProduct:
    def __init__(self, product: WebElement) -> None:
        """Initialise the property of a product.

        :param product: WebElement
        """
        self._product: WebElement = product

    def get_name(self) -> str:
        """Method that gets product name.

        :return: string
        """
        return self._product.find_element(*Locators.PizzaPageLocators.LOCATOR_PIZZA_NAME).text

    def click_add_to_cart(self) -> None:
        """Method that add item to the cart.

        :return:None
        """
        self._product.find_element(*Locators.PizzaPageLocators.LOCATOR_ADD_TO_CART).click()
