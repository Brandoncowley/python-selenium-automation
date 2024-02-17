# HOMEWORK 2 = LOCATORS

# This task does not need to execute, but rather documents the ways that we can locate elements on a webpage.
# In this example, navigate to the Amazon sign-in page (http://tinyurl.com/36mr4wxy)
# and using locators, find the following elements on the page:

# Amazon logo
# Email field
# Continue button
# Conditions of use link
# Privacy Notice link
# Need help link
# Forgot your password link
# Other issues with Sign-In link
# Create your Amazon account button

# Use search by ID and search by XPATH to your advantage.

# -----------------------------------------------

# Amazon logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
# Email field
driver.find_element(By.ID, "ap_email")
# Continue button
driver.find_element(By.ID, "continue")
# Conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
# Privacy Notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
# Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
# Forgot your password link
driver.find_element(By.ID, "auth-fpp-link-bottom")
# Other issues with Sign-In link
driver.find_element(By.ID, "ap-other-signin-issues-link")
# Create your Amazon account button
driver.find_element(By.ID, "createAccountSubmit")
