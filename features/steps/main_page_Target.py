from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target_page(context):
    # context.driver.get("https://target.com")
    context.app.main_page.open_main() # modified to page object format


@when('Search for {product}')
def search_for_product(context, product):
    # context.driver.find_element(By.ID, 'search').send_keys(product)
    # context.driver.find_element(By.CSS_SELECTOR, '[aria-label="search"]').click()
    # sleep(6)
    context.app.main_page.search(product)  # modified to page object format


@then('Verify {expected_result} in search results')
def verify_search_result(context, expected_result):
    # actual_result = context.driver.find_element(By.CSS_SELECTOR, '[data-test="results-facets-row"]').text
    # assert expected_result in actual_result, f"Expected to find {expected_result}, got {actual_result}"
    # print("Product Search test passed")
    context.app.search_results_page.verify_search_result(expected_result)


@when('Click on Cart icon')
def click_on_cart_icon(context):
    # context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/CartLink"]').click()
    context.app.main_page.click_cart()  # modified to page object format


@when('Click on Sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/AccountLink"]').click()


@when('Click Sign in on side menu')
def click_side_menu_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="accountNav-signIn"]').click()


@then('Verify header is present')
def verify_header(context):
    context.driver.find_element(By.CSS_SELECTOR, '[class*="UtilityHeaderWrapper"]')


@then('Verify header has {number} links')
def verify_header_has_links(context, number):
    number = int(number) # need to convert number to integer, otherwise it will fail
    links = context.driver.find_elements(By.CSS_SELECTOR, '[class*="UtilityHeaderLinksContainer"] a')
    print(links)
    assert len(links) == number, f'Expected {number} links, got {len(links)} instead.'

