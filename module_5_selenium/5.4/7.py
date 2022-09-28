from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "http://parsinger.ru/selenium/7/7.html"
with webdriver.Chrome() as browser:
    browser.get(url)

    values = browser.find_elements(By.TAG_NAME, value='option')
    addition = sum(int(value.text) for value in values)

    browser.find_element(By.ID, value='input_result').send_keys(addition)

    browser.find_element(By.ID, value='sendbutton').click()
    time.sleep(5)