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

# open the url
driver.get('https://www.amazon.com/')

# Search by CSS, ID -> uses $$('#value')
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox') # driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox') # with starting tag

# Search by CSS, Class -> uses $$('.value')
driver.find_element(By.CSS_SELECTOR, '.nav-input') # driver.find_element(By.Class, 'nav-input')
driver.find_element(By.CSS_SELECTOR, '.nav-input.nav-progressive-element') # multiple classes
driver.find_element(By.CSS_SELECTOR, 'input.nav-input') # with starting tag

# Search by CSS, all other attributes -> uses $$('[key value pair]')
driver.find_element(By.CSS_SELECTOR, '[placeholder="Search Amazon"]') # driver.find_element(By., 'twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, '[placeholder="Search Amazon"][name="field-keywords"]') # with multiples
driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search Amazon"]') # with tag

# Search with partial attribute -> uses * before equal sign
driver.find_element(By.CSS_SELECTOR, '[data-csa-c-content-id*="cs_bestsellers"]')
