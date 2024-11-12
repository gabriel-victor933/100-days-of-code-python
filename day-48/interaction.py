from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.NAME,'fName')
first_name.send_keys('Gabriel')

last_name = driver.find_element(By.NAME,'lName')
last_name.send_keys('Santana')

email = driver.find_element(By.NAME,'email')
email.send_keys('gabriel@gmail.com')

button_submit = driver.find_element(By.XPATH,'/html/body/form/button')
button_submit.click()