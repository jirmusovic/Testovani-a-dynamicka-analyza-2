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


@given(u'web browser is on the "Products" page')
def step_impl(context):
    context.driver.get("http://opencart:8080/administration/index.php?route=catalog/product&user_token=a3b7ce9a0e82039b72c2894ec8b54bf2")



@when(u'administrator clicks on "Add new"')
def step_impl(context):
    element = context.driver.find_element(By.CSS_SELECTOR, ".btn-danger")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, ".float-end > .btn-primary")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, ".d-lg-none:nth-child(1)")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, ".float-end > .btn-primary")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element, 0, 0).perform()
    context.driver.find_element(By.CSS_SELECTOR, ".btn > .fa-plus").click()


@then(u'"Add Product" page is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Add Product"


@given(u'web browser is on the "Add Product" page')
def step_impl(context):
    context.driver.get("http://opencart:8080/administration/index.php?route=catalog/product|form&user_token=a3b7ce9a0e82039b72c2894ec8b54bf2")


@given(u'all of the information is filled out')
def step_impl(context):
    context.driver.get("http://opencart:8080/administration/index.php?route=catalog/product|form&user_token=a3b7ce9a0e82039b72c2894ec8b54bf2")


@when(u'administrator clicks on "Save"')
def step_impl(context):
    element = context.driver.find_element(By.CSS_SELECTOR, ".float-end > .btn-primary")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    context.driver.find_element(By.CSS_SELECTOR, ".float-end > .btn-primary").click()
    element = context.driver.find_element(By.CSS_SELECTOR, ".float-end > .btn-primary")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element, 0, 0).perform()


@then(u'product is modified')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Success"


@when(u'administrator clicks on "Categories"')
def step_impl(context):
    context.driver.get("http://opencart:8080/administration/index.php?route=common/dashboard&user_token=a3b7ce9a0e82039b72c2894ec8b54bf2")
    context.driver.find_element(By.CSS_SELECTOR, "#button-menu > .fa-solid").click()
    context.driver.find_element(By.LINK_TEXT, "Catalog").click()
    context.driver.find_element(By.LINK_TEXT, "Categories").click()


@then(u'page with "Category list" is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Category list"
