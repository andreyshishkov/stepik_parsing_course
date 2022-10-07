from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


url = "http://parsinger.ru/expectations/3/index.html"
options = webdriver.ChromeOptions()
options.headless = True
with webdriver.Chrome(options=options) as browser:
    browser.get(url)

    element = WebDriverWait(browser, 3).until(
        ec.element_to_be_clickable([By.ID, 'btn'])
    ).click()

    while True:
        title = browser.execute_script('return document.title;')
        if title == '345FDG3245SFD':
            result = browser.find_element(By.ID, 'result').text
            break
print(result)
