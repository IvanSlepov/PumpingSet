from src.pages.base_page import BasePage
from src.pages.locators.checkout_locators import CheckoutLocators
from src.testData.test_pages import TestPages
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement


class CheckoutPage(BasePage):
    def __init__(self, driver: Remote):
        """Initialize driver and objects to works with checkout.

        :param driver: Remote
        """
        super().__init__(driver)
        self.payment_detail = PaymentDetailsComponent(self._driver)
        self.your_order = YourOrderComponent(self._driver)

    def go_to_checkout_page(self) -> None:
        """Method that proceeds to Checkout page.

        :return:None
        """
        self._driver.get(TestPages.CHECKOUT_PAGE)


class YourOrderComponent:
    def __init__(self, driver: Remote) -> None:
        """Initialize your order component.

        :param driver: Remote
        :return: None
        """
        self._driver: Remote = driver

    def products_in_shopping_cart(self) -> list:
        """Method that returns list of WebElements to work with each product in shopping cart.

        :return: list.
        """
        products_list: list = []
        products = self._driver.find_elements(*CheckoutLocators.LOCATOR_PRODUCTS_IN_CART)
        for product in products:
            products_list.append(product.text)
        return products_list

    def check_product_in_shopping_cart(self, product_in_cart) -> bool:
        """Method that check product in product cart.

        :return: Boolean
        """
        products = self.products_in_shopping_cart()
        for product in products:
            if product == product_in_cart:
                return True


class PaymentDetailsComponent:
    def __init__(self, driver) -> None:
        """Initialize your Payment Detail component.

        :param driver: Remote
        :return: None
        """
        self._driver = driver

    def details_of_purchase(self, your_name, phone, email, street, premise_number) -> None:
        """Method that fills form in Payment Detail.

        :return: None
        """

        self._driver.find_element(*CheckoutLocators.LOCATOR_NAME).send_keys(your_name)

        self._driver.find_element(*CheckoutLocators.LOCATOR_BILLING_PHONE).send_keys(Keys.CLEAR + phone)

        self._driver.find_element(*CheckoutLocators.LOCATOR_EMAIL).send_keys(Keys.CLEAR + email)

        self._driver.find_element(*CheckoutLocators.LOCATOR_STREET).send_keys(Keys.CLEAR + street)

        self._driver.find_element(*CheckoutLocators.LOCATOR_PREMISE_NUMBER).send_keys(Keys.CLEAR + premise_number)
