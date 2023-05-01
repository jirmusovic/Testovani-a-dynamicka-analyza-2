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


@given(u'user is not registered')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=common/home")


@given(u'user clicks on "My Account" icon')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".show > .d-none").click()


@when(u'user clicks on "Register" icon')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Register").click()


@then(u'page with "Register Account" is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Register Account"


@given(u'web browser is on the "Register Account" page')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=account/register")


@given(u'"Personal Details" is filled')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").click()
    context.driver.find_element(By.ID, "input-firstname").send_keys("joe")
    context.driver.find_element(By.ID, "input-lastname").click()
    context.driver.find_element(By.ID, "input-lastname").send_keys("black")
    context.driver.find_element(By.ID, "input-email").click()
    context.driver.find_element(By.ID, "input-email").send_keys("hello@world.com")
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("123456")


@given(u'"I have read and agree to the Privacy Policy" is checked')
def step_impl(context):
    context.driver.find_element(By.NAME, "agree").click()


@when(u'user clicks on "Continue"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()


@then(u'page with "Your Account Has Been Created!" is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Your Account Has Been Created!"


@given(u'web browser is on the "Login" page')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=account/login")


@given(u'"E-mail Address" is correctly filled out')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").click()
    context.driver.find_element(By.ID, "input-email").send_keys("bv@bv.bv")


@given(u'Password is correctly filled out')
def step_impl(context):
    context.driver.find_element(By.ID, "input-password").click()
    context.driver.find_element(By.ID, "input-password").send_keys("bvbvbv")


@when(u'user clicks on "Login"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(5)").click()


@then(u'"My Account" page is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "My Account"
