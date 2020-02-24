import os
from selenium import webdriver
from pathlib import Path  # python3 only
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options


# Прописываем путь до файла .env и подгружаем оттуда переменные окружения
env_path = Path(r'C:\Users\Roman\PycharmProjects\beautymarket ads.env')
load_dotenv(dotenv_path=env_path)


class Webdriver():
    def func_webdriver(): #todo переделать на класс, чтобы вызывая экземляр класса оставалась одна и та же сессия
        path = os.getenv('chromedriver')
        options = Options()
        options.add_argument("--window-size=1500,1000")
        options.add_argument("--disable-notifications")
        # options.add_argument('--headless')
        driver = webdriver.Chrome(executable_path=path, options=options)
        return driver
    driver = func_webdriver()



# def func_webdriver(): #todo переделать на класс, чтобы вызывая экземляр класса оставалась одна и та же сессия
#     path = os.getenv('chromedriver')
#     options = Options()
#     options.add_argument("--window-size=1500,1000")
#     # options.add_argument('--headless')
#     driver = webdriver.Chrome(executable_path=path, options=options)
#     return driver


def main():
    driver = Webdriver().driver


if __name__ == '__main__':
    main()

