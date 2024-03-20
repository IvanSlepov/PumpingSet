import time

from src.pages.base_page import BasePage
from src.testData.test_pages import TestPages
from src.testData.order_test_data import OrderDetails
from src.pages.locators.checkout_locators import CheckoutLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement


class CheckoutPage(BasePage):
    def __init__(self, driver: Remote):
        """Initialize driver and objects to works with checkout.
        :param driver: Remote
        """
        super().__init__(driver)
        self.cart_product_list: list = []

    def go_to_checkout_page(self) -> None:
        """Method that proceeds to Checkout page.
        :return:None
        """
        self._driver.get(TestPages.CHECKOUT_PAGE)

    def open_the_cart(self, time=10) -> None:
        """Method that opens the cart
        :return:None
        """
        (WebDriverWait(self._driver, time).
         until(EC.visibility_of_element_located(CheckoutLocators.LOCATOR_CART),
               message=f"Can't find elements by locator {CheckoutLocators.LOCATOR_CART} ").click())

    def get_list_of_products_in_cart(self) -> list:
        """Fills product_list with OrderComponent class instances.
        This method must be called before you start working with product methods.
        :return: list of OrderComponent class instances
        """
        cart_products: list = self._driver.find_elements(*CheckoutLocators.LOCATOR_PRODUCTS_IN_CART)
        for cart_product in cart_products:
            self.cart_product_list.append(OrderComponent(cart_product))
        return self.cart_product_list

    def get_cart_products_name_list(self) -> list:
        """Method that returns list with names of the products in cart.
        :return: list
        """
        cart_product_names_list: list = []
        for cart_product in self.cart_product_list:
            cart_product_names_list.append(cart_product.get_name())
        return cart_product_names_list

    def proceed_if_the_product_is_in_cart(self, cart_product_name: str) -> None:
        """Method that proceeds with checkout if required product is in the cart.
         :param: string
         :return: None
         """
        for cart_product in self.cart_product_list:
            if cart_product.get_name() == cart_product_name:
                cart_product.click_proceed_with_checkout()

    def place_order(self) -> None:
        """Method that places the order.
         :return: None
         """
        complete_order_data = PaymentDetailsComponent(self._driver)
        complete_order_data.details_of_purchase(
            OrderDetails.NAME,
            OrderDetails.PHONE,
            OrderDetails.EMAIL,
            OrderDetails.STREET,
            OrderDetails.PREMISE_NUMBER
        )

        time.sleep(1)
        (WebDriverWait(self._driver, 10).
         until(EC.visibility_of_element_located(CheckoutLocators.LOCATOR_ORDER_BUTTON),
               message=f"Can't find elements by locator {CheckoutLocators.LOCATOR_ORDER_BUTTON} ").click())

    def confirm_order_placed(self) -> bool:
        """Method that confirms if the order was placed.
         :return: was_placed
         """
        was_placed: bool = False
        was_placed = (WebDriverWait(self._driver, 10).
                      until(EC.visibility_of_element_located(CheckoutLocators.LOCATOR_ORDER_PLACED),
                            message=f"Can't find elements by locator {CheckoutLocators.LOCATOR_ORDER_PLACED} ")
                      .is_displayed())
        return was_placed


class OrderComponent:
    def __init__(self, cart_product: WebElement) -> None:
        """Initialise the property of a product.
        :param cart_product: WebElement
        """
        self._cart_product: WebElement = cart_product

    def get_name(self) -> str:
        """Method that gets product name.
        :return: string
        """
        return self._cart_product.find_element(*CheckoutLocators.LOCATOR_PRODUCTS_IN_CART_NAME).text

    def click_proceed_with_checkout(self) -> None:
        """Method that add item to the cart.
        :return:None
        """
        self._cart_product.find_element(*CheckoutLocators.LOCATOR_PROCEED_WITH_CHECKOUT).click()


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

        self._driver.find_element(*CheckoutLocators.LOCATOR_BILLING_PHONE).send_keys(Keys.CLEAR, phone)

        self._driver.find_element(*CheckoutLocators.LOCATOR_EMAIL).send_keys(Keys.CLEAR, email)

        self._driver.find_element(*CheckoutLocators.LOCATOR_STREET).send_keys(Keys.CLEAR, street)

        (self._driver.find_element(*CheckoutLocators.LOCATOR_PREMISE_NUMBER).send_keys
         (Keys.CLEAR, premise_number))
