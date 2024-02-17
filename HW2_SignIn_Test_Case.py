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
# HOMEWORK 2 = SIGN IN PAGE - TARGET

# In this task we need to use the Target website to identify and click the Sign-in button,
# and verify that the correct page has been opened
# -------------------------------------------------

# open the url
driver.get('https://www.target.com/')

# click Sign In button
driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']").click()

# wait for 2 sec, see the side nav open
sleep(2)

# click Sign In on side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

# wait for 2 sec
sleep(2)

# Verify that the sign-in page opened
expected_result = "Sign in with password"
actual_result = driver.find_element(By.ID, "login").text

assert expected_result == actual_result, f"Expected to find {expected_result}, got {actual_result}"
print("Sign in test passed")

driver.quit()
