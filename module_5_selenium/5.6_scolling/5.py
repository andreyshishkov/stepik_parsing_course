from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = "http://parsinger.ru/infiniti_scroll_2/"
options = webdriver.ChromeOptions()
options.headless = True
delta_x, delta_y = 1, 500
with webdriver.Chrome(options=options) as browser:
    browser.get(url)
    browser.maximize_window()

    scroll_container = browser.find_element(By.XPATH,
                                            value='//*[@id="scroll-container"]/div')
    for _ in range(20):
        ActionChains(browser).move_to_element(scroll_container)\
            .scroll_by_amount(delta_x, delta_y).perform()

    num_tags = browser.find_element(By.ID, 'scroll-container')\
        .find_elements(By.TAG_NAME, value='p')
    assert len(num_tags) == 100, f"wrong number of tags: {len(num_tags)}"
    addition = sum(int(x.text) for x in num_tags)
print(addition)

