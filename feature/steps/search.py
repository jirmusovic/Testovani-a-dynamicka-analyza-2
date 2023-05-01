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

"""@given('web browser is on the home page')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=common/home")


@when('when you search "iPhone"')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("iPhone")
    context.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)
    search_input = context.driver.find_element_by_css_selector("#search-input")
    search_input.send_keys("iPhone")
    search_input.submit()


@then('you get the iPhone page')
def step_impl(context):
    product_title = context.driver.find_element_by_css_selector("#product-title")
    assert product_title.text == "iPhone" """

@given(u'the "Apple Cinema 30" exists')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=common/home")


@when(u'user searches for a Apple Cinema 30"')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("Apple Cinema 30")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()


@then(u'page with Apple Cinema 30" is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Search - Apple Cinema 30"


@given(u'the iMac exists')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=common/home")


@when(u'user searches for a iMac')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("iMac")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()


@then(u'page with iMac is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Search - iMac"


@given(u'the Samsung SyncMaster 941BW exists')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=common/home")


@when(u'user searches for a Samsung SyncMaster 941BW')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("Samsung SyncMaster 941BW")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()


@then(u'page with Samsung SyncMaster 941BW is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Search - Samsung SyncMaster 941BW"


@given(u'the Samsung Galaxy Tab 10.1 exists')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=common/home")


@when(u'user searches for a Samsung Galaxy Tab 10.1')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("Samsung Galaxy Tab 10.1")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()


@then(u'page with Samsung Galaxy Tab 10.1 is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Search - Samsung Galaxy Tab 10.1"


@given(u'the HTC Touch HD exists')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=common/home")


@when(u'user searches for a HTC Touch HD')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("HTC Touch HD")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()


@then(u'page with HTC Touch HD is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Search - HTC Touch HD"


@given(u'the iPhone exists')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=common/home")


@when(u'user searches for a iPhone')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("iPhone")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()


@then(u'page with iPhone is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Search - iPhone"


@given(u'the Palm Treo Pro exists')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=common/home")


@when(u'user searches for a Palm Treo Pro')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("Palm Treo Pro")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()


@then(u'page with Palm Treo Pro is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Search - Palm Treo Pro"


@given(u'the Canon EOS 5D exists')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=common/home")


@when(u'user searches for a Canon EOS 5D')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("Canon EOS 5D")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()


@then(u'page with Canon EOS 5D is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Search - Canon EOS 5D"


@given(u'the Nikon D300 exists')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=common/home")


@when(u'user searches for a Nikon D300')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("Nikon D300")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()


@then(u'page with Nikon D300 is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Search - Nikon D300"


@given(u'the HP LP3065 exists')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=common/home")


@when(u'user searches for a HP LP3065')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("HP LP3065")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()


@then(u'page with HP LP3065 is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Search - HP LP3065"


@given(u'the iPod Classic exists')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=common/home")


@when(u'user searches for a iPod Classic')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("iPod Classic")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()


@then(u'page with iPod Classic is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Search - iPod Classic"


@given(u'the MacBook exists')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=common/home")


@when(u'user searches for a MacBook')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("MacBook")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()


@then(u'page with MacBook is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Search - MacBook"


@given(u'the MacBook Air exists')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=common/home")


@when(u'user searches for a MacBook Air')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("MacBook Air")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-light").click()


@then(u'page with MacBook Air is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Search - MacBook Air"


@given(u'the product does not exist')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=common/home")


@when(u'user searches for a not-product')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").click()
    context.driver.find_element(By.NAME, "search").send_keys("hello")
    context.driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)


@then(u'page with no-matched-product text')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "There is no product that matches the search criteria."


@given(u'the product exist')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb/product/macbook")


@when(u'user clicks on "Add to Cart"')
def step_impl(context):
    context.driver.find_element(By.ID, "button-cart").click()


@then(u'product should be added to cart')
def step_impl(context):
    element = context.driver.find_element(By.ID, "button-cart")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()
    element = context.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(context.driver)
    actions.move_to_element(element, 0, 0).perform()


@given(u'a web browser is on "Shopping Cart" page')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=checkout/cart")


@when(u'user clicks on "Checkout"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".float-end > .btn").click()


@then(u'page with "Checkout" is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Checkout"


@given(u'a web browser is on "Checkout" page')
def step_impl(context):
    context.driver.get("http://opencart:8080/en-gb?route=checkout/checkout")


@given(u'personal information is filled out')
def step_impl(context):
    context.driver.find_element(By.ID, "input-shipping-firstname").click()
    context.driver.find_element(By.ID, "input-shipping-firstname").send_keys("john")
    context.driver.find_element(By.ID, "input-shipping-lastname").click()
    context.driver.find_element(By.ID, "input-shipping-lastname").send_keys("doe")
    context.driver.find_element(By.ID, "input-shipping-address-1").click()
    context.driver.find_element(By.ID, "input-shipping-address-1").send_keys("pecaboo 42")
    context.driver.find_element(By.ID, "input-shipping-city").click()
    context.driver.find_element(By.ID, "input-shipping-city").send_keys("nowhere")
    context.driver.find_element(By.ID, "input-shipping-country").click()
    dropdown = context.driver.find_element(By.ID, "input-shipping-country")
    dropdown.find_element(By.XPATH, "//option[. = 'Bangladesh']").click()
    context.driver.find_element(By.ID, "input-shipping-zone").click()
    dropdown = context.driver.find_element(By.ID, "input-shipping-zone")
    dropdown.find_element(By.XPATH, "//option[. = 'Dhaka']").click()
    context.driver.find_element(By.ID, "button-shipping-address").click()


@given(u'shipping method is filled out')
def step_impl(context):
    context.driver.find_element(By.ID, "input-shipping-method").click()
    dropdown = context.driver.find_element(By.ID, "input-shipping-method")
    dropdown.find_element(By.XPATH, "//option[. = 'Flat Shipping Rate - $5.00']").click()


@given(u'payment method is filled out')
def step_impl(context):
    context.driver.find_element(By.ID, "input-payment-method").click()
    dropdown = context.driver.find_element(By.ID, "input-payment-method")
    dropdown.find_element(By.XPATH, "//option[. = 'Cash On Delivery']").click()


@when(u'user clicks on "Confirm Order"')
def step_impl(context):
    context.driver.find_element(By.ID, "button-confirm").click()


@then(u'page with "Your order has been placed!" is shown')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Your order has been placed!"
