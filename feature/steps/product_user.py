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


@given(u'product was ordered by customer')
def step_impl(context):
    context.driver.get("http://opencart:8080/administration/index.php?route=common/dashboard&user_token=fbd9c4703f8266440a1184fa2225be64")



@when(u'web browser is on the "Customers" page')
def step_impl(context):
    context.driver.find_element(By.ID, "button-menu").click()
    context.driver.find_element(By.LINK_TEXT, "Customers").click()
    context.driver.find_element(By.CSS_SELECTOR, "#collapse-5 > li:nth-child(1) > a").click()


@then(u'"Customer List" is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Customer List"


@when(u'administrator clicks on "Edit"')
def step_impl(context):
    element = context.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) .btn:nth-child(1)")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element, 0, 0).perform()
    context.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) .fa-pencil").click()


@then(u'administrator can edit customer\'s profile')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Customers"
