import time

from behave import *
from selenium import webdriver
# from behave_webdriver.steps import *
# - looks like we do not need this import as of 2024
# it causes the error:TypeError: metaclass conflict:
# the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases


from src.pages.base_page import BasePage
from src.pages.pizza_page import PizzaPage
from src.pages.checkout_page import CheckoutPage
from src.testData.test_items import TestItems


@given('User proceeds to the Panda Pizza main page')
def step(context):
    context.main_page = BasePage(context.browser)
    context.main_page.go_to_site()


@then("If there's a blocking message, they close it")
def step(context):
    context.main_page.close_blocking_message()


@then("They proceed to the Pizza Page")
def step(context):
    context.pizza_page = PizzaPage(context.browser)
    context.pizza_page.go_to_pizza_page()


@then("They choose some pizza and add it to the cart")
def step(context):
    context.pizza_page.generate_product_list()
    time.sleep(2)
    context.pizza_page.add_product_to_shopping_cart(TestItems.TEST_PRODUCT_NAME)
    assert context.pizza_page.check_items_in_cart() == TestItems.TEST_PRODUCT_QUANTITY


@then("User opens the order cart")
def step(context):
    context.checkout_page = CheckoutPage(context.browser)
    context.checkout_page.open_the_cart()
    time.sleep(2)


@then("User continues with checkout if required product is in cart")
def step(context):
    context.checkout_page.get_list_of_products_in_cart()
    time.sleep(2)
    context.checkout_page.proceed_if_the_product_is_in_cart(TestItems.TEST_PRODUCT_NAME)


@then('User populates the required data and places the order')
def step(context):
    time.sleep(2)
    context.checkout_page.place_order()


@then("User waits for the placed order confirmation")
def step(context):
    time.sleep(2)
    assert context.checkout_page.confirm_order_placed()
    time.sleep(5)
