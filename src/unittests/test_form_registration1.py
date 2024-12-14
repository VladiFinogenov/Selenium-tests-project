import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.link = "http://suninjuly.github.io/registration2.html"
        cls.browser = webdriver.Chrome()
        cls.browser.get(cls.link)

    def test_registration(self):
        # Filling out the mandatory fields
        first_name = self.browser.find_element(By.CSS_SELECTOR, ".first_class input[placeholder*='name']")
        first_name.send_keys("Ivan")

        last_name = self.browser.find_element(By.CSS_SELECTOR, ".second_class input[placeholder*='name']")
        last_name.send_keys("Petrov")

        email = self.browser.find_element(By.CSS_SELECTOR, ".third_class input[placeholder*='email']")
        email.send_keys("test@example.com")

        # Submitting the filled form
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Waiting for the new page to load
        time.sleep(2)

        # Finding the element with the welcome text
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        # Asserting that the expected text matches the text on the page
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    @classmethod
    def tearDownClass(cls):
        # Waiting to visually assess the results
        time.sleep(5)
        # Closing the browser after all actions
        cls.browser.quit()


if __name__ == "__main__":
    unittest.main()