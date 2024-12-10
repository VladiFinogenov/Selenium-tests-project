import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация веб-драйвера
browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открываем страницу
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ожидаем, пока цена не станет \$100 (не менее 12 секунд)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )


    # Нажимаем на кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    print(y)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    # Отправляем форму
    submit_button = WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    submit_button.click()


finally:
    time.sleep(5)  # Ждем, чтобы увидеть результат
    browser.quit()
