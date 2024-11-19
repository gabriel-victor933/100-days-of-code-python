from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

class InternetSpeedTwitterBot:
    def __init__(self, twitter_username, twitter_password):
        self.twitter_username = twitter_username
        self.twitter_password = twitter_password
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')

        time.sleep(10)

        self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()

        time.sleep(75)

        download_speed = float(self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        upload_speed = float(self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        return download_speed, upload_speed

    def tweet_at_provider(self, download, upload):
        self.driver.get('https://twitter.com/i/flow/signup')

        time.sleep(10)

        self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/button/span/span').click()

        time.sleep(10)

        input_username = self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')

        input_username.send_keys(self.twitter_username)

        self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div').click()

        time.sleep(10)

        input_password = self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')

        input_password.send_keys(self.twitter_password)

        self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button').click()

        time.sleep(10)

        tweet_box = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        
        tweet_box.send_keys(f"{download} - {upload}")

        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button').click()


