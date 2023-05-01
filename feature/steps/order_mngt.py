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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


@given(u'the administrator is logged in')
def step_impl(context):
    context.driver.get("http://opencart:8080/administration/index.php?route=common/login")
    context.driver.find_element(By.CSS_SELECTOR, ".btn").click()


@given(u'web browser is on the "Customers" page')
def step_impl(context):
    context.driver.get("http://opencart:8080/administration/index.php?route=common/login")


@when(u'order is placed')
def step_impl(context):
    driver = webdriver.Chrome()
    text_present = EC.text_to_be_present_in_element((By.XPATH, "//div[@class='some_class']"), "joe black")
    WebDriverWait(driver, timeout=10).until(text_present)


@then(u'information about order is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Default"


@then(u'information about customer is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "hello@world.com"


@given(u'web browser is on the "Product Returns" page')
def step_impl(context):
    context.driver.get("http://opencart:8080/administration/index.php?route=common/dashboard&user_token=fbd9c4703f8266440a1184fa2225be64")
    context.driver.find_element(By.CSS_SELECTOR, "#button-menu > .fa-solid").click()
    context.driver.find_element(By.LINK_TEXT, "Sales").click()
    context.driver.find_element(By.LINK_TEXT, "Returns").click()


@then(u'information about return is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Product Returns"


@given(u'web browser is on the "Orders" page')
def step_impl(context):
    context.driver.get("http://opencart:8080/administration/index.php?route=sale/order&user_token=fbd9c4703f8266440a1184fa2225be64")


@given(u'product is ordered')
def step_impl(context):
    driver = webdriver.Chrome()
    text_present = EC.text_to_be_present_in_element((By.XPATH, "//div[@class='some_class']"), "joe black")
    WebDriverWait(driver, timeout=10).until(text_present)


@when(u'administrator clicks on "View"')
def step_impl(context):
    element = context.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) .btn")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element, 0, 0).perform()
    context.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) .fa-solid").click()


@then(u'order information is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Product Returns"
