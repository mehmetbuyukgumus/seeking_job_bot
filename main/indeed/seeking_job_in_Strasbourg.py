from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import key_words_indeed

browser = webdriver.Firefox()
url = 'https://fr.indeed.com/'
browser.get(url)
time.sleep(3)
reject_cookies = browser.find_element(By.XPATH, "//*[@id='onetrust-reject-all-handler']")
reject_cookies.click()
time.sleep(1)
search_input = browser.find_element(By.XPATH, "//*[@id='text-input-what']")
search_input.send_keys(key_words_indeed.key_words["job"])
time.sleep(1)
city = browser.find_element(By.XPATH, "//*[@id='text-input-where']")
city.clear()
time.sleep(1)
city.send_keys(key_words_indeed.key_words["City2"])
time.sleep(1)
search_button = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/span/div[3]/div[1]/div/div/div/div/form/button")
search_button.click()
job_posting = browser.find_elements(By.CLASS_NAME, "css-5lfssm eu4oa1w0")
for title in job_posting:
    all_title = browser.find_elements(By.CLASS_NAME, "jcs-JobTitle css-jspxzf eu4oa1w0")
    key_words_indeed.db.jobs_in_Paris["Title"] = all_title
    