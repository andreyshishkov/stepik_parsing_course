from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


url = "http://parsinger.ru/expectations/4/index.html"
options = webdriver.ChromeOptions()
options.headless = True
with webdriver.Chrome() as browser:
    browser.get(url)

    element = WebDriverWait(browser, 3).until(
        ec.element_to_be_clickable([By.ID, 'btn'])
    ).click()
    WebDriverWait(browser, 20).until(ec.title_contains('JK8HQ'))
    result = browser.execute_script('return document.title;')
print(result)
