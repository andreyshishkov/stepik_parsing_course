from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/scroll/2/index.html"
options = webdriver.ChromeOptions()
options.headless = True

with webdriver.Chrome(options=options) as browser:
    browser.get(url)

    inputs = browser.find_elements(By.TAG_NAME, value='input')
    for input_ in inputs:
        input_.click()

    addition = 0
    values = browser.find_elements(By.TAG_NAME, 'span')
    for value in values:
        if value.text:
            addition += int(value.text)
    print(addition)
