from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv
from internetSpeedTwitterBot import InternetSpeedTwitterBot

load_dotenv()

TWITTER_USERNAME = os.environ['TWITTER_USERNAME']
TWITTER_PASSWORD = os.environ['TWITTER_PASSWORD']

speedTwitterBot = InternetSpeedTwitterBot(TWITTER_USERNAME,TWITTER_PASSWORD)

download, upload = speedTwitterBot.get_internet_speed()

speedTwitterBot.tweet_at_provider(download,upload)

