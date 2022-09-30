from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/scroll/3/"
options = webdriver.ChromeOptions()
options.headless = True

with webdriver.Chrome(options=options) as browser:
    browser.get(url)

    inputs = browser.find_elements(By.TAG_NAME, value='input')
    for input_ in inputs:
        input_.click()

    addition = 0
    values = browser.find_elements(By.TAG_NAME, 'span')
    for value, input_ in zip(values, inputs):
        if value.text:
            addition += int(input_.get_attribute('id'))
    print(addition)
