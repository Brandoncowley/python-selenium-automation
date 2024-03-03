from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target Circle page')
def open_target_circle_page(context):
    context.driver.get("https://www.target.com/circle")


@given('Open Target Help page')
def open_target_help_page(context):
    context.driver.get("https://help.target.com/help")
    sleep(2)


@then('Verify Circle Benefits are present')
def verify_circle_benefits(context):
    context.driver.find_element(By.CSS_SELECTOR, '[class*="styles__BenefitsGrid"]')


@then('Verify page has {number} benefits boxes')
def verify_benefits_count(context, number):
    number = int(number)
    boxes = context.driver.find_elements(By.CSS_SELECTOR, '[class*="styles__BenefitTextContainer"]')
    print(len(boxes))
    assert len(boxes) == number, f'Expected {number} links, got {len(boxes)} instead.'


@when('Add item to cart')
def add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '[id*="addToCartButtonOrTextIdFor"]').click()
    sleep(4)
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="shippingButton"]').click()
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, '[href="/cart"]').click()
    sleep(2)


@then('Verify UI elements are present')
def verify_help_ui(context):
    # Target Help
    context.driver.find_element(By.CSS_SELECTOR, '[class="custom-h2"]')
    # Search Box
    context.driver.find_element(By.CSS_SELECTOR, '[class="search-input"]')
    # Search Icon
    context.driver.find_element(By.CSS_SELECTOR, '[class*="search-btn"]')
    # First "help" container
    context.driver.find_elements(By.CSS_SELECTOR, '[class="grid_6"]')
    # Second "help" container
    contact_grid = context.driver.find_elements(By.CSS_SELECTOR, '[class*="boxSmallr"]')
    print(len(contact_grid))
    # Browse all Help pages
    context.driver.find_element(By.ID, 'divID1')


@then('Verify first Help section has {number} elements')
def verify_first_help_section(context, number):
    number = int(number)
    help_grid = context.driver.find_elements(By.CSS_SELECTOR, '[class="grid_6"]')
    print(len(help_grid))
    assert len(help_grid) == number, f'Expected {number} links, got {len(help_grid)} instead.'

