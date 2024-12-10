import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num_element1 = browser.find_element(By.ID, 'num1')
    num_element2 = browser.find_element(By.ID, 'num2')
    num1 = num_element1.text
    num2 = num_element2.text

    sum_num = int(num1) + int(num2)

    print(sum_num)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum_num))


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()