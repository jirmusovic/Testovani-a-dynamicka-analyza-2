import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest
from behave import *


@given(u'web browser is on the home page')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=common/home")

@when(u'user clicks on "My Account"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".show > .d-none").click()


@then(u'column with My Account is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "My Account"


@then(u'column with Order History is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "My Orders"


@then(u'column with Transactions is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Transactions"


@then(u'column with Downloads is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Downloads"


@then(u'column with Logout is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Logout"

@given(u'web browser is on the "Order History" page')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=account/order&customer_token=533c0722e064e82f1a4761f228")


@given(u'an item is ordered')
def step_impl(context):
    element = context.driver.find_element(By.CSS_SELECTOR, ".btn-info")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element, 0, 0).perform()
    context.driver.find_element(By.CSS_SELECTOR, ".fa-eye").click()


@when(u'user clicks on "View"')
def step_impl(context):
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element, 0, 0).perform()
    context.driver.find_element(By.CSS_SELECTOR, ".fa-eye").click()


@then(u'"Order History" page is shown with ordered product')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Order History"


@given(u'web browser is on the "My Account" page')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=account/account&customer_token=c9d11f25fcb14693808911d87a")


@when(u'user clicks on "View your order history"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "View your order history").click()


@then(u'"Order History" page is shown with no product')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "You have not made any previous orders!"
