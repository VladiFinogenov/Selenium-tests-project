import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    print(y)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    time.sleep(1)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radiobutton1 = browser.find_element(By.ID, 'peopleRule')
    print(radiobutton1.is_selected())
    radiobutton2 = browser.find_element(By.ID, 'robotsRule')
    print(radiobutton2.is_selected())
    if radiobutton1.is_selected():
        radiobutton2.click()
    else:
        radiobutton1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()