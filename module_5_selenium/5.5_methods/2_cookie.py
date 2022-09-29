from selenium import webdriver

url = "https://parsinger.ru/methods/3/index.html"
options = webdriver.ChromeOptions()
options.headless = True
with webdriver.Chrome(options=options) as browser:
    browser.get(url)

    cookies = browser.get_cookies()
    amount = 0
    for cookie in cookies:
        amount += int(cookie['value'])
    print(amount)
