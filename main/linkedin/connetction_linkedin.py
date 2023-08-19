from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import key_words_linkedin

def connecting_to_linkedin():
    #Connecting to web site
    url = 'https://tr.linkedin.com/'
    linkedin_browser = webdriver.Firefox()
    linkedin_browser.get(url)
    time.sleep(3)
    #Closing the cookies that is banned to reaching sign in area
    closed_cookies_linkedin = linkedin_browser.find_element(By.XPATH, "/html/body/div[1]/div/section/div/div[2]/button[2]")
    time.sleep(1)
    closed_cookies_linkedin.click()
    time.sleep(1)
    #Reacing sign in area and click it
    log_in_linkedin_button = linkedin_browser.find_element(By.XPATH, "/html/body/nav/div/a[2]")
    log_in_linkedin_button.click()
    time.sleep(1)
    #Entry the username and password
    usename_linkedin = linkedin_browser.find_element(By.XPATH, "//*[@id='username']")
    usename_linkedin.send_keys(key_words_linkedin.key_words["mail_adress"])
    time.sleep(1)
    password_linkedin = linkedin_browser.find_element(By.XPATH, "//*[@id='password']")
    password_linkedin.send_keys(key_words_linkedin.key_words["password"])
    time.sleep(1)
    #Log in Linkedin
    log_in = linkedin_browser.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button")
    log_in.click()
