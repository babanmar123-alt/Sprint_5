# Локаторы элементов на страницах

from selenium.webdriver.common.by import By

class MainPageLocators:
    """Локаторы для главной страницы"""
    
    # Кнопка «Войти в аккаунт» на главной
    LOGIN_BUTTON_MAIN = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    
    # Кнопка «Личный кабинет» (в правом верхнем углу)
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//a[@href='/account']")
    
    # Кнопка «Конструктор» (в верхнем меню)
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//a[@href='/']")
    
    # Логотип Stellar Burgers
    LOGO = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a")
    
    # Разделы в конструкторе
    BUNS_SECTION = (By.XPATH, ".//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, ".//span[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, ".//span[text()='Начинки']/parent::div")
    
    # Активная вкладка (для проверки переключения разделов)
    ACTIVE_TAB = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current')]")


class LoginPageLocators:
    """Локаторы для страницы входа"""
    
    # Поле ввода Email
    EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")
    
    # Поле ввода Пароля
    PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")
    
    # Кнопка «Войти»
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    
    # Ссылка «Зарегистрироваться» (на странице входа)
    REGISTER_LINK = (By.XPATH, ".//a[@href='/register']")
    
    # Ссылка «Восстановить пароль» (на странице входа)
    FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[@href='/forgot-password']")


class RegisterPageLocators:
    """Локаторы для страницы регистрации"""
    
    # Поле ввода Имени
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    
    # Поле ввода Email
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    
    # Поле ввода Пароля
    PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")
    
    # Кнопка «Зарегистрироваться»
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    
    # Сообщение об ошибке (для некорректного пароля)
    ERROR_MESSAGE = (By.XPATH, ".//p[contains(@class, 'input__error')]")


class ForgotPasswordPageLocators:
    """Локаторы для страницы восстановления пароля"""
    
    # Кнопка «Войти» на странице восстановления
    LOGIN_BUTTON_FORGOT = (By.XPATH, ".//a[@href='/login']")


class AccountPageLocators:
    """Локаторы для страницы личного кабинета"""
    
    # Кнопка «Выйти» в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выйти']")
    
    # Заголовок страницы (для проверки, что мы в личном кабинете)
    PROFILE_HEADER = (By.XPATH, ".//a[contains(@class, 'Account_link_active')]")