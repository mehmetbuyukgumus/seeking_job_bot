from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import key_words_indeed

browser = webdriver.Firefox()
url = 'https://www.indeed.fr'
browser.get(url)
time.sleep(3)
reject_cookies = browser.find_element(By.XPATH, "//*[@id='onetrust-reject-all-handler']")
reject_cookies.click()
time.sleep(1)
connecting = browser.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/div/div[2]/div[2]/div[2]/a")
connecting.click()
time.sleep(1)
sending_email_adress = browser.find_element(By.XPATH, "//*[@id='ifl-InputFormField-3']")
sending_email_adress.click()
time.sleep(2)
sending_email_adress.send_keys(key_words_indeed.key_words["mail_adress"])
time.sleep(1)
to_continue = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[2]/div/form/button")
to_continue.click()
password = browser.find_element(By.XPATH, "//*[@id='ifl-InputFormField-146']")
password.send_keys(key_words_indeed.key_words["password"])
time.sleep(10)
to_continue_1 = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[2]/div/form[1]/button")
to_continue_1.click()