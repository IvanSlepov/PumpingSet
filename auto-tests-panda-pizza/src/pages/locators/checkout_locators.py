from selenium.webdriver.common.by import By


class CheckoutLocators:
    """Locators for Checkout Page."""

    """Cart dropdown and product list inside"""
    LOCATOR_CART: tuple[str, str] = (By.CSS_SELECTOR, ".arrow_down")
    LOCATOR_CART_FOR_SUSHI: tuple[str, str] = (By.XPATH, "//div[@id='header-cart-mini']//img[@alt='Вiдкрити корзину']")
    LOCATOR_PRODUCTS_IN_CART: tuple[str, str] = (By.XPATH, '//*[@id="header-cart-full"]/div/ul/li')
    LOCATOR_PRODUCTS_IN_CART_NAME: tuple = (By.CSS_SELECTOR, "a")

    """Button to continue with checkout"""
    LOCATOR_PROCEED_WITH_CHECKOUT: tuple[str, str] = (By.XPATH, '//*[@id="header-cart-full"]/div/a')

    """Button to continue with sushi checkout"""
    LOCATOR_PROCEED_WITH_SUSHI_CHECKOUT: tuple[str, str] = (By.XPATH, '//*[@id="header-cart-mini"]/div/a')

    """Checkout data"""
    LOCATOR_NAME: tuple[str, str] = (By.XPATH, "//form[@id='order-form']/input[@name='name']")
    LOCATOR_BILLING_PHONE: tuple[str, str] = (By.XPATH, "//form[@id='order-form']/input[@name='phone']")
    LOCATOR_EMAIL: tuple[str, str] = (By.XPATH, "//form[@id='order-form']/input[@name='email']")
    LOCATOR_STREET: tuple[str, str] = (By.XPATH, "//form[@id='order-form']/input[@name='street']")
    LOCATOR_PREMISE_NUMBER: tuple[str, str] = (By.XPATH, "//form[@id='order-form']/input[@name='number']")

    """Confirm order button"""
    LOCATOR_ORDER_BUTTON: tuple[str, str] = (By.XPATH, "//form[@id='order-form']//input[@value='ОФОРМИТИ']")

    """Order placed message"""
    LOCATOR_ORDER_PLACED: tuple[str, str] = \
        (
            By.XPATH, "//div[@id='header-cart-full']//div[@class='desk-basket-thanks']"
        )

    """Locator to check pizza number of items in cart"""
    LOCATOR_NUMBER_OF_ITEMS_IN_CART = \
        (
            By.XPATH, "//div[@id='header-cart-full']//span[@class='number']"
        )

    """Locator to check sushi sets number of items in cart"""
    LOCATOR_NUMBER_OF_SUSHI_SET_ITEMS_IN_CART = \
        (
            By.XPATH, "//div[@id='header-cart-mini']//span[@class='number']"
        )
