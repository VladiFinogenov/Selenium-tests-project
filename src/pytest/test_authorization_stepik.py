import math
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


params_link = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
]

def calculate_answer():
    return str(math.log(int(time.time())))

@pytest.mark.parametrize('link_task', params_link)
def test_authorization_stepik(browser, link_task):
    # Переход на страницу задачи
    browser.get(link_task)

    # Нажимаем на кнопку "Вход" (если она доступна)
    authorization_btn = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.ID, "ember469"))
    )
    authorization_btn.click()

    # Вводим логин
    form_login = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.NAME, "login"))
    )
    form_login.send_keys('Finogenov.V.A@yandex.ru')

    # Вводим пароль
    form_password = browser.find_element(By.NAME, "password")
    form_password.send_keys('Volgograd@2024')

    # Нажимаем кнопку "Вход"
    login_btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_btn.click()

    # Ожидание завершения авторизации
    WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "navbar__profile"))
    )

    # После авторизации переходим на страницу задания
    answer = calculate_answer()
    text_answer = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[placeholder*='Напишите ваш']"))
    )
    text_answer.clear()
    text_answer.send_keys(answer)

    # Нажимаем кнопку "Отправить"
    send_btn = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    send_btn.click()

    # Ожидаем фидбек и проверяем текст
    feedback = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )
    feedback_text = feedback.text

    # Проверяем, что текст в опциональном фидбеке совпадает с "Correct!"
    assert feedback_text == "Correct!", f"Expected 'Correct!', but got '{feedback_text}'"












