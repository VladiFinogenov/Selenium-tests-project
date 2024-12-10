## Selenium

### Описание проекта
Авто-тесты.

### Технологии
- Python 3.11
- Selenium 4.27.1

### Запуск проекта

#### Клонирование и установка зависимостей

1. Склонировать репозиторий:
```
git clone  ...
```

2. Перейти в папку с проектом:
```
cd src/
```

3. Создать и активировать виртуальное окружение:
- Windows:
```
C:\> python -m venv venv
C:\> venv\Scripts\activate.bat
```

- Linux / Mac:
```
$ python3 -m venv .venv
$ source .venv/bin/activate
```

4. Установить зависимости:
```
(.venv) pip install -r requirements.txt
```

5. В корневой папке проекта (Selenium-tests-project/) необходимо создать .env файл
```
```
Примечание:
```
(Пока что нет ни каких данных)
```

#### Настройка драйвера ChromeDriver

1. Проверьте версию драйвера:
```
google-chrome --version  (131.0.6778.108)
```

2. Скачайте соответствующий ChromeDriver:
```
wget https://chromedriver.storage.googleapis.com/XX.0.XXXX.XX/chromedriver_linux64.zip
```
Примечание:
```
заменив XX.0.XXXX.XX на вашу версию из п.1:
```
Пример последней стабильной версии на 7.112.2024:
```
wget https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.87/linux64/chromedriver-linux64.zip
```
3. Распакуйте скачанный файл:
```
unzip chromedriver-linux64.zip
```
4. Переместите разархивированный файл с СhromeDriver в нужную папку и разрешите запускать chromedriver как исполняемый файл:
```
sudo mv chromedriver /usr/local/bin/
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod +x /usr/local/bin/chromedriver
```
5. Проверьте установку:
```
chromedriver --version
```

