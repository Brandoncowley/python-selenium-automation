from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# -------------------------------------------------
# HOMEWORK 2 (OPTIONAL) = PRODUCT SEARCH - TARGET

# Build a test case yourself from scratch to search for a product on Target ,
# make sure it works, and you remember selenium commands.
# ASSESSMENT CRITERIA:
# Locators are built correctly and point to the correct web elements
# Test case runs and works correctly

# -------------------------------------------------

# open the url
driver.get('https://www.target.com/')

# Locate and populate the Search bar
driver.find_element(By.ID, 'search').send_keys('Television')

# wait for 2 sec to validate input
sleep(2)

# click on Search icon
driver.find_element(By.XPATH, "//button[@aria-label='search']").click()

# wait for 2 sec
sleep(2)

# Verification process
expected_result = 'results'
actual_result = driver.find_element(By.XPATH, "//div[@data-test='results-facets-row']").text

assert expected_result in actual_result, f"Expected to find {expected_result}, got {actual_result}"
print("Product Search test passed")

driver.quit()
