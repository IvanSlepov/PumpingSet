from selenium.webdriver.common.by import By


class BasePageLocators:
    """Base page locators"""

    LOCATOR_BLOCKING_MESSAGE = (By.XPATH, '//*[@id="modal-share"]/div/div[2]/div/div[2]/button')
