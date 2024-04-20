from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from behave import given, when, then
from time import sleep


@then('Verify empty cart')
def verify_empty_cart(context):
    # context.driver.find_element(By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
    context.app.cart_page.verify_empty_cart() # modified to page object format


@then('Verify Sign in form opens')
def verify_sign_in_form(context):
    context.driver.find_element(By.CSS_SELECTOR, '#login')


@then('Verify item added to cart')
def verify_item_added(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="cartItem"]')

