from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.XPATH,'/html/body/div[3]/div[6]/div[9]')

timeout = time.time() + 60*5
interval = time.time() + 5

while True:
    cookie.click()

    if time.time() > timeout:
        break

    if time.time() > interval:
        cookies_total = int(driver.find_element(By.ID, 'money').text)
        
        store_elems = driver.find_elements(By.CSS_SELECTOR, 'div#rightPanel div#store > div')

        last_clickable = None
        for elem in store_elems:
            if elem.get_attribute('class') != 'grayed':
                last_clickable = elem

        if last_clickable is not None:
            last_clickable.click()

        interval = time.time() + 5


time.sleep(2)   
driver.close()
