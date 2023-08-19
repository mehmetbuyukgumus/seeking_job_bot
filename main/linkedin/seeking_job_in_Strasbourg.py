from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import key_words_linkedin

#Connecting to web site
url2 = 'https://www.linkedin.com/feed/?trk=guest_homepage-basic_nav-header-signin'
job_seeking_browser = webdriver.Firefox()
job_seeking_browser.get(url2)
time.sleep(3)
#Start to looing job postings
jop_positngs = job_seeking_browser.find_element(By.XPATH, "/html/body/div[5]/header/div/nav/ul/li[3]/a")
jop_positngs.click()
time.sleep(1)
#Seeking job
job_title = job_seeking_browser.find_element(By.XPATH, "//*[@id='jobs-search-box-keyword-id-ember300']")
job_title.click()
time.sleep(1)
job_title.send_keys(key_words_linkedin.key_words["job"])
time.sleep(2)
#Writing City for Seeking Job
city = job_seeking_browser.find_element(By.XPATH, "//*[@id='jobs-search-box-location-id-ember300']")
city.click()
time.sleep(2)
city.send_keys(key_words_linkedin.key_words["City2"])
time.sleep(1)
city.send_keys(Keys.ENTER)

