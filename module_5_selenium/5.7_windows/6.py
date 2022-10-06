from selenium import webdriver
from selenium.webdriver.common.by import By
from itertools import product

url = "https://parsinger.ru/window_size/2/index.html"
window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
options = webdriver.ChromeOptions()
options.headless = True

with webdriver.Chrome(options=options) as browser:
    browser.get(url)

    for x, y in product(window_size_x, window_size_y):
        browser.set_window_size(x, y)

        result = browser.find_element(By.ID, 'result').text
        if result:
            d = {'width': x, 'height': y}
            break
print(d)
