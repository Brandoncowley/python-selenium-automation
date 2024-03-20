from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from behave import given, when, then
from time import sleep


@given('Open Target product A-54551690')
def open_pants_product(context):
    context.driver.get("https://www.target.com/p/A-54551690")
    sleep(4)


COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, '[class*="StyledVariationSelectorImage"] [class*="StyledHeaderWrapperDiv"]')


@then('Verify user can click all colors')
def click_all_colors(context):
    expected_color = ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
    actual_color = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[1]
        actual_color.append(selected_color)

    assert actual_color == expected_color, f"Expected options = {expected_color}, instead got {actual_color}"