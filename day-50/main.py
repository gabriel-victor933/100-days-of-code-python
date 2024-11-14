from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv()

facebook_email = os.environ['FACEBOOK_EMAIL']
facebook_password = os.environ['FACEBOOK_PASSWORD']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.implicitly_wait(10)

    url = 'https://tinder.com/'

    driver.get(url)

    button_accepted = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')

    button_accepted.click()

    button_login = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')

    button_login.click()

    time.sleep(2)

    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]').click()

    base_window = driver.window_handles[0]
    fb_login_window = driver.window_handles[1]
    
    driver.switch_to.window(fb_login_window)

    input_email = driver.find_element(By.NAME,'email')
    input_pass = driver.find_element(By.NAME,'pass')
    

    input_email.send_keys(facebook_email)
    input_pass.send_keys(facebook_password)

    driver.find_element(By.NAME,'login').click()

    time.sleep(2)

    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div').click()

    driver.switch_to.window(driver.window_handles[0])

    time.sleep(2)

    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]/div[2]/div[2]').click()

    time.sleep(2)

    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]/div[2]/div[2]').click()

    while True: 
        time.sleep(5)
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button').click()
        

except Exception as e:
    print('Error: ',e)
finally:
    #driver.quit()
    pass