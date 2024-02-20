from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target page')
def open_target_page(context):
    context.driver.get("https://target.com")


@when('Click on Cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/CartLink"]').click()
    sleep(2)

@then('Verify empty cart')
def verify_empty_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
    sleep(2)


@when('Click on Sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/AccountLink"]').click()
    sleep(2)


@when('Click Sign in on side menu')
def click_side_menu_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="accountNav-signIn"]').click()
    sleep(2)


@then('Verify Sign in form opens')
def verify_sign_in_form(context):
    context.driver.find_element(By.CSS_SELECTOR, '#login')
    sleep(4)



