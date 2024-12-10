import time

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    # link = 'http://suninjuly.github.io/registration1.html'
    link = 'http://suninjuly.github.io/registration1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.first')
    input_first_name.send_keys('Ivan')
    input_last_name = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.second')
    input_last_name.send_keys('Ivanov')
    input_email = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.third')
    input_email.send_keys('Email')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, 'h1')
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert welcome_text == 'Congratulations! You have successfully registered!'

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    browser.quit()
