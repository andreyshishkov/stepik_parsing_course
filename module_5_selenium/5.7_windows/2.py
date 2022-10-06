from selenium import webdriver
from selenium.webdriver.common.by import By


url = "https://parsinger.ru/blank/modal/3/index.html"
options = webdriver.ChromeOptions()
options.headless = True
with webdriver.Chrome(options=options) as browser:
    browser.get(url)
    browser.maximize_window()

    buttons = browser.find_elements(By.CLASS_NAME,
                                    value='buttons'
                                    )
    assert len(buttons) == 100
    for button in buttons:
        button.click()

        alert = browser.switch_to.alert
        code = alert.text
        alert.accept()

        browser.find_element(By.ID, value='input').send_keys(code)
        browser.find_element(By.ID, value='check').click()

        result = browser.find_element(By.ID, value='result').text
        if result != 'Неверный пин-код':
            break
print(result)
