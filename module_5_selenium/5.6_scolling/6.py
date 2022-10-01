from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = "http://parsinger.ru/infiniti_scroll_3/"
options = webdriver.ChromeOptions()
# options.headless = True


def get_value_from_window(driver, scroll_container, idx):
    """Calculate sum from single window"""
    delta_x, delta_y = 1, 500
    for _ in range(10):
        ActionChains(driver).move_to_element(scroll_container.find_element(By.TAG_NAME, 'div')).\
            scroll_by_amount(delta_x, delta_y).perform()
    value_tags = driver.find_element(By.ID, value=f'scroll-container_{idx}').\
        find_elements(By.TAG_NAME, value='span')
    assert len(value_tags) == 100, f"Wrong number of tags: {len(value_tags)}"
    return sum(int(value.text) for value in value_tags)


with webdriver.Chrome(options=options) as browser:
    browser.get(url)
    browser.maximize_window()

    scroll_containers = browser.find_elements(By.XPATH,
                                              value='//*[starts-with(@id,"scroll-container_")]')
    assert len(scroll_containers) == 5, f'Current length: {len(scroll_containers)}'

    addition = 0
    for i, container in enumerate(scroll_containers, start=1):
        addition += get_value_from_window(browser, container, i)
print(addition)
