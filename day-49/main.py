from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import time

load_dotenv()

EMAIL = os.environ['LINKEDIN_EMAIL']
PASSWORD = os.environ['LINKEDIN_PASSWORD']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

url = 'https://www.linkedin.com/jobs/search/?currentJobId=4035254065&f_AL=true&keywords=Desenvolvedor%20Python&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true'

driver.implicitly_wait(10)

try:
    driver.get(url)

    button_signin = driver.find_element(By.XPATH,'/html/body/div[4]/div/div/section/div/div/div/div[2]/button')
    button_signin.click()

    input_email = driver.find_element(By.NAME, 'session_key')
    input_password = driver.find_element(By.NAME, 'session_password')

    input_email.send_keys(EMAIL)
    input_password.send_keys(PASSWORD)
                                            
    button_signin = driver.find_element(By.XPATH,'/html/body/div[4]/div/div/section/div/div/form/div[2]/button')
    button_signin.click()

    time.sleep(60000)

    jobs_search_results = driver.find_elements(By.CLASS_NAME,'jobs-search-results__list-item')

    len(jobs_search_results)

    for job_ele in jobs_search_results:
        job_ele.click()
        time.sleep(2)
        button_save = driver.find_element(By.CLASS_NAME,'jobs-save-button')
        button_save.click()
        time.sleep(2)

except Exception as e:
    print('error',e)
finally:
    driver.quit()