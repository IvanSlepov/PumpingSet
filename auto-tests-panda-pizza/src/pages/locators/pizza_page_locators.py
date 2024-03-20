from selenium.webdriver.common.by import By


class PizzaPageLocators:
    """Locators for Pizza Page."""

    LOCATOR_PIZZAS = (By.XPATH, "//div[@id='pitsa']/div[@class='desktop-product-wrapper']/div")

    LOCATOR_PIZZA_NAME = (By.CSS_SELECTOR, "a")
    LOCATOR_ADD_TO_CART = (By.CLASS_NAME, "buttons")

