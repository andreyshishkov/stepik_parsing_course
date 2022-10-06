from selenium import webdriver
from selenium.webdriver.common.by import By


url = "http://parsinger.ru/blank/modal/2/index.html"
options = webdriver.ChromeOptions()
options.headless = True
with webdriver.Chrome(options=options) as browser:
    browser.get(url)
    browser.maximize_window()

    buttons = browser.find_elements(By.CLASS_NAME, value='buttons')
    assert len(buttons) == 100
    for button in buttons:
        button.click()
        alert = browser.switch_to.alert
        alert.accept()

        result = browser.find_element(By.ID, value='result').text
        if result:
            break
print(result)
