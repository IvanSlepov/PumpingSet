import selenium.webdriver as webdriver
from behave import *


@fixture
def browser_firefox(context):
    context.browser = webdriver.Firefox()
    context.browser.maximize_window()
    yield context.browser
    context.browser.delete_all_cookies()
    context.browser.quit()


@fixture
def browser_chrome(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    yield context.browser
    context.browser.delete_all_cookies()
    context.browser.quit()


def before_all(context):
    context.choose_browser = int(input("In which browser do you want to run test(1 - Chrome, 2 - Firefox):\n"))


def before_scenario(context, scenario):
    if context.choose_browser == 1:
        use_fixture(browser_chrome, context)
    elif context.choose_browser == 2:
        use_fixture(browser_firefox, context)