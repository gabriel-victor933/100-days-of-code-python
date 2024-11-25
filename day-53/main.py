import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

forms_link = 'https://forms.gle/DaPFSU3L9KCiCPtp9'

zillow_page = requests.get('https://appbrewery.github.io/Zillow-Clone')

soup = BeautifulSoup(zillow_page.text,'html.parser')

articles = soup.select('div.grid-search-results ul > li article')

infos = []

for article in articles:
    data = {}
    link_ele = article.select('div.StyledPropertyCardDataWrapper > a',limit=1)[0]
    data['link'] = link_ele.get('href')

    data['address'] = link_ele.get_text().strip()

    price_ele = article.select('span.PropertyCardWrapper__StyledPriceLine')[0]
    data['price'] = price_ele.get_text()

    infos.append(data)
    

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(5)

driver.get(forms_link)

for data in infos:

    input_address = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_address.send_keys(data['address'])

    input_price = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_price.send_keys(data['price'])

    input_link = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_link.send_keys(data['link'])

    driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div').click()

    time.sleep(2)

    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

    time.sleep(2)


driver.close()