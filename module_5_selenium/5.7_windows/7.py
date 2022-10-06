from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://parsinger.ru/blank/3/index.html"
options = webdriver.ChromeOptions()
options.headless = True
with webdriver.Chrome(options=options) as browser:
    browser.get(url)

    buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
    assert len(buttons) == 10
    for button in buttons:
        button.click()

    windows = browser.window_handles[1:]
    addition = 0
    for window in windows:
        browser.switch_to.window(window)
        num = int(browser.execute_script('return document.title;'))
        addition += num
print(addition)
