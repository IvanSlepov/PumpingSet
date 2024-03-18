from selenium.webdriver.common.by import By


class CheckoutLocators:
    """Locators for Checkout Page."""
    LOCATOR_PRODUCTS_IN_CART: tuple[str, str] = \
        (
            By.XPATH, "//div[@id='header-cart-mini']//ul/li/div[@class='product-title']/a[@href='#']"
        )
    LOCATOR_CART: tuple[str, str] = (By.XPATH, "//div[@id='header-cart-full']/a[@href='javascript:void(0)']")
    LOCATOR_PROCEED_WITH_CHECKOUT: tuple[str, str] = (By.XPATH, "//div[@id='header-cart-full']/div/a[@href='#']")
    LOCATOR_NAME: tuple[str, str] = (By.XPATH, "//form[@id='order-form']/input[@name='name']")
    LOCATOR_BILLING_PHONE: tuple[str, str] = (By.XPATH, "//form[@id='order-form']/input[@name='phone']")
    LOCATOR_EMAIL: tuple[str, str] = (By.XPATH, "//form[@id='order-form']/input[@name='email']")
    LOCATOR_STREET: tuple[str, str] = (By.XPATH, "//form[@id='order-form']/input[@name='street']")
    LOCATOR_PREMISE_NUMBER: tuple[str, str] = (By.XPATH, "//form[@id='order-form']/input[@name='number']")
    LOCATOR_ORDER_BUTTON: tuple[str, str] = (By.XPATH, "//form[@id='order-form']//input[@value='ОФОРМИТИ']")
    LOCATOR_NUMBER_OF_ITEMS_IN_CART = \
        (
            By.XPATH, "//div[@id='header-cart-mini']//span[@class='number']"
        )