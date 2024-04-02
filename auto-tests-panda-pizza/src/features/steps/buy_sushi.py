import time

from behave import *
from selenium import webdriver
# from behave_webdriver.steps import *
# - looks like we do not need this import as of 2024
# it causes the error:TypeError: metaclass conflict:
# the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases

from src.pages.base_page import BasePage
from src.pages.sushi_page import SushiPage
from src.pages.checkout_page import CheckoutPage
from src.testData.test_items import TestItems


@given('User proceeds to the Panda Pizza main page.')
def step(context):
    context.main_page = BasePage(context.browser)
    context.main_page.go_to_site()


@then("If there's a blocking message, they close it.")
def step(context):
    context.main_page.close_blocking_message()


@then("They proceed to the Sushi Page.")
def step(context):
    context.sushi_page = SushiPage(context.browser)
    context.sushi_page.go_to_sushi_page()


@then("If there's another blocking message, they close it.")
def step(context):
    context.main_page.close_blocking_message()


@then("They choose some sushi set and add it to the cart.")
def step(context):
    context.sushi_page.generate_product_list()
    context.sushi_page.add_product_to_shopping_cart(TestItems.SUSHI_PRODUCT_NAME)
    assert context.sushi_page.check_items_in_cart() == TestItems.SUSHI_PRODUCT_QUANTITY


@then("User opens the order cart.")
def step(context):
    context.checkout_page = CheckoutPage(context.browser)
    context.checkout_page.open_the_sushi_cart()


@then("User continues with checkout if required product is in cart.")
def step(context):
    context.checkout_page.get_list_of_products_in_cart()
    context.checkout_page.proceed_if_the_sushi_is_in_cart(TestItems.SUSHI_PRODUCT_NAME)


@then('User populates the required data and places the order.')
def step(context):
    context.checkout_page.place_order()


@then("User waits for the placed order confirmation.")
def step(context):
    assert context.checkout_page.confirm_order_placed()
    time.sleep(5)
