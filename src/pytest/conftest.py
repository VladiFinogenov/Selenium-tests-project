import pytest
from selenium import webdriver

def pytest_addoption(parser):
    """Функция которую pytest автоматически вызывает при запуске"""
    parser.addoption('--language', action='store', default='ru', help='Choose language for testing')

@pytest.fixture
def browser(request):
    language = request.config.getoption('language')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()