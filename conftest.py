# Файл с фикстурами для тестов
# Файл с фикстурами для тестов



import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from data import Urls


@pytest.fixture
def driver():
    """
    Фикстура для запуска браузера.
    По умолчанию — Google Chrome.
    """
    # Настройки для Chrome
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Создаём драйвер Chrome
    driver = webdriver.Chrome(options=chrome_options)
    
    # Открываем главную страницу
    driver.get(Urls.MAIN_PAGE)
    
    yield driver  # Передаём драйвер в тест
    
    # После теста закрываем браузер
    driver.quit()


@pytest.fixture
def register_new_user(driver):
    """
    Фикстура для регистрации нового пользователя.
    Возвращает email и пароль созданного пользователя.
    """
    from helpers import generate_unique_email, generate_password
    
    # Генерируем уникальный email и пароль
    email = generate_unique_email()
    valid_password, invalid_password = generate_password()
    
    # Переходим на страницу регистрации
    driver.get(Urls.REGISTER_PAGE)
    
    # Возвращаем данные для использования в тестах
    return {
        "email": email,
        "password": valid_password
    }