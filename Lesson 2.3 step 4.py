from selenium import webdriver

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit_el = browser.find_element_by_css_selector("button[type='submit']")
    submit_el.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    input_el = browser.find_element_by_id("answer")
    input_el.send_keys(y)

    submit_el = browser.find_element_by_css_selector("button[type='submit']")
    submit_el.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
