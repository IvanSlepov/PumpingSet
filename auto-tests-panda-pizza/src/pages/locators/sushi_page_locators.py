from selenium.webdriver.common.by import By


class SushiPageLocators:
    """Locators for Pizza Page."""

    LOCATOR_SUSHI_SETS = (By.XPATH, "//div[@id='nabori']/div[@class='desktop-product-wrapper']/div")

    LOCATOR_SUSHI_SET_NAME = (By.CSS_SELECTOR, "a")
    LOCATOR_ADD_TO_CART = (By.CLASS_NAME, "buttons")