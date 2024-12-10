import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(current_dir)  # Поднимаемся на уровень выше
file_path = os.path.join(parent_dir, 'resource/file.txt')


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, "form input[name=firstname]")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.CSS_SELECTOR, "form input[name=lastname]")
    last_name.send_keys("Petrov")
    email = browser.find_element(By.CSS_SELECTOR, "form input[name=email]")
    email.send_keys("test@example.com")

    # ждем загрузки страницы
    time.sleep(2)

    file = browser.find_element(By.ID, "file")
    file.send_keys(file_path)


    button = browser.find_element(By.CSS_SELECTOR, "form button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()