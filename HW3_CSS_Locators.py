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

# HOMEWORK 3 = CSS LOCATORS

# This task does not need to execute, but rather documents the ways that we can locate elements on a webpage.
# In this example, navigate to the Amazon sign-in page (http://tinyurl.com/bk6ssfxt)
# and using CSS locators, find the following elements on the page:

# Amazon logo
# Create Account text
# Name input field
# Phone number or Email input field
# Password input field
# Password input field helper text
# Re-enter password input field
# Continue (create amazon Account) button
# Conditions of Use link
# Privacy Notice link
# Sign in link

# Use CSS locators to your advantage, and if not possible, use XPath locators.

# -----------------------------------------------

# Amazon logo
driver.find_element(By.CSS_SELECTOR, '[aria-label="Amazon"]')
# Create Account text
driver.find_element(By.XPATH, '//h1[@class="a-spacing-small"]')
# Name input field
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
# Mobile number / Email input field
driver.find_element(By.CSS_SELECTOR, '#ap_email')
# Password input field
driver.find_element(By.CSS_SELECTOR, '#ap_password')
# Password input field helper text
driver.find_element(By.XPATH, '.a-alert-inline-info')
# Re-enter password input field
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
# Continue button
driver.find_element(By.CSS_SELECTOR, '#continue')
# Conditions of Use link
driver.find_element(By.CSS_SELECTOR, '[href*="condition"]')
# Privacy Notice link
driver.find_element(By.CSS_SELECTOR, '[href*="register_notification_privacy"]')
# Sign in link
driver.find_element(By.CSS_SELECTOR, '[href*="signin"]')
