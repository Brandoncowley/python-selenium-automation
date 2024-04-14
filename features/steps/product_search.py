from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
LISTINGS = (By.CSS_SELECTOR, '[data-test="@web/site-top-of-funnel/ProductCardWrapper"]')
PRODUCT_TITLE = (By.CSS_SELECTOR, '[data-test="product-title"]')
PRODUCT_IMG = (By.CSS_SELECTOR, '[class*="StyledProductCardImageWrapper"]')


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'


@then('Verify that every product has a name and an image')
def verify_products_name_and_img(context):
    # Scroll down the webpage
    context.driver.execute_script("window.scrollBy(0, 2000);")
    sleep(2)
    # Scroll down the webpage again
    context.driver.execute_script("window.scrollBy(0, 2000);")

    all_products = context.driver.find_elements(*LISTINGS)
    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        print(title)
        assert title, 'Product title not found in listing'
        product_img = product.find_element(*PRODUCT_IMG)
        assert product_img, 'Product image not found in listing'
