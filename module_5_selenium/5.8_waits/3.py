from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

url = 'http://parsinger.ru/expectations/6/index.html'
options = webdriver.ChromeOptions()
options.headless = True
with webdriver.Chrome(options=options) as browser:
    browser.get(url)

    WebDriverWait(browser, 4).until(
        ec.element_to_be_clickable([By.ID, 'btn'])
    ).click()

    location = (By.CLASS_NAME, 'Y1DM2GR')
    WebDriverWait(browser, 30).until(
        ec.presence_of_element_located(location)
    )
    result = browser.find_element(*location).text
print(result)
