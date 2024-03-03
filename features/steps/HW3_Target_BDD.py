from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify empty cart')
def verify_empty_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
    sleep(2)


@then('Verify Sign in form opens')
def verify_sign_in_form(context):
    context.driver.find_element(By.CSS_SELECTOR, '#login')
    sleep(4)


@then('Verify item added to cart')
def verify_item_added(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="cartItem"]')
    sleep(4)
