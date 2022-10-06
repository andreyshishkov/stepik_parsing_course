from selenium import webdriver
from selenium.webdriver.common.by import By
from math import sqrt


sites = ['http://parsinger.ru/blank/1/1.html',
         'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html',
         'http://parsinger.ru/blank/1/5.html',
         'http://parsinger.ru/blank/1/6.html',
         ]

options = webdriver.ChromeOptions()
options.headless = True
values = []
with webdriver.Chrome(options=options) as browser:
    for i, site in enumerate(sites, start=1):
        browser.execute_script(f'window.open("{site}", "_blank{i}");')
    windows = browser.window_handles[1:]
    for window in windows:
        browser.switch_to.window(window)
        browser.find_element(By.CLASS_NAME, 'checkbox_class').click()

        values.append(int(browser.find_element(By.ID, 'result').text))


result = sum(sqrt(x) for x in values)
print(round(result, 9))
