from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://parsinger.ru/selenium/1/1.html"
input_values = ['Андрей',
                'Шишков',
                'Васильевич',
                '21',
                'Краснодар',
                'shishkoffandrey@yandex.ru',
                ]
with webdriver.Chrome() as browser:
    browser.get(url)
    inputs = browser.find_elements(By.CLASS_NAME, value='form')
    for form, value in zip(inputs, input_values):
        form.send_keys(value)
    browser.find_element(By.ID, 'btn').click()
    time.sleep(5)
