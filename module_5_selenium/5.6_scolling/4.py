from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

url = "http://parsinger.ru/infiniti_scroll_1/"
options = webdriver.ChromeOptions()
options.headless = True
with webdriver.Chrome(options=options) as browser:
    browser.maximize_window()
    browser.get(url)
    time.sleep(1)

    list_inputs = []
    addition = 0
    while True:
        span_tags = browser.find_element(By.ID, "scroll-container").find_elements(By.TAG_NAME, 'span')
        inputs = browser.find_element(By.ID, "scroll-container").find_elements(By.TAG_NAME, 'input')
        for span, input_ in zip(span_tags, inputs):
            if input_ not in list_inputs:
                input_.send_keys(Keys.DOWN)
                input_.click()
                list_inputs.append(input_)
                time.sleep(1)

                addition += int(span.text)
        last_span = span_tags[-1]
        try:
            if last_span.get_attribute('class') == 'last-of-list':
                break
        except AttributeError:
            continue
print(addition)

