from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://parsinger.ru/blank/modal/4/index.html"
options = webdriver.ChromeOptions()
options.headless = True
with webdriver.Chrome(options=options) as browser:
    browser.get(url)
    browser.maximize_window()

    codes = [x.text for x in browser.find_elements(By.CLASS_NAME, 'pin')]
    for code in codes:
        browser.find_element(By.ID, 'check').click()
        prompt = browser.switch_to.alert
        prompt.send_keys(code)
        prompt.accept()

        result = browser.find_element(By.ID, 'result').text
        if result != 'Неверный пин-код':
            break
print(result)
