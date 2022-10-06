from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/window_size/1/'
options = webdriver.ChromeOptions()
options.headless = True
with webdriver.Chrome(options=options) as browser:
    browser.get(url)
    browser.set_window_size(555, 555)

    result = browser.find_element(By.ID, 'result').text
print(result)
