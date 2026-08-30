# tests/test_personal_account.py — тесты для личного кабинета

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from data import Urls
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators, AccountPageLocators
from helpers import generate_unique_email, generate_password


class TestPersonalAccount:

    @pytest.fixture(autouse=True)
    def login_user(self, driver):
        email = generate_unique_email()
        valid_password, _ = generate_password()
        name = "Тест"
        
        driver.get(Urls.REGISTER_PAGE)
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(valid_password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        
        driver.get(Urls.LOGIN_PAGE)
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(valid_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def test_go_to_personal_account(self, driver):
        """Тест 7: Переход в личный кабинет"""
        driver.get(Urls.MAIN_PAGE)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        wait = WebDriverWait(driver, 5)
        profile_header = wait.until(EC.presence_of_element_located(AccountPageLocators.PROFILE_HEADER))
        assert profile_header.is_displayed()

    def test_go_to_constructor_from_account(self, driver):
        """Тест 8: Переход из личного кабинета в конструктор по клику на «Конструктор»"""
        driver.get(Urls.MAIN_PAGE)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(AccountPageLocators.PROFILE_HEADER))
        
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        order_button = wait.until(EC.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        assert order_button.is_displayed()

    def test_go_to_constructor_from_logo(self, driver):
        """Тест 9: Переход из личного кабинета в конструктор по клику на логотип"""
        driver.get(Urls.MAIN_PAGE)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(AccountPageLocators.PROFILE_HEADER))
        
        driver.find_element(*MainPageLocators.LOGO).click()
        order_button = wait.until(EC.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        assert order_button.is_displayed()

    def test_logout(self, driver):
        """Тест 10: Выход из аккаунта"""
        driver.get(Urls.MAIN_PAGE)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(AccountPageLocators.PROFILE_HEADER))
        
        driver.find_element(*AccountPageLocators.LOGOUT_BUTTON).click()
        login_button = wait.until(EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        assert login_button.is_displayed()