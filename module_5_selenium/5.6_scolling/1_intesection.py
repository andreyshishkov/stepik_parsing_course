from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/scroll/4/index.html"
options = webdriver.ChromeOptions()
options.headless = True
with webdriver.Chrome(options=options) as browser:
    browser.get(url)

    buttons = browser.find_elements(By.CLASS_NAME, value='btn')

    addition = 0
    for button in buttons:
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
        cur_num = browser.find_element(By.ID, value='result').text
        addition += int(cur_num)
    print(addition)
    