# Обновлено для pull request
# tests/test_login.py — тесты для входа

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from data import Urls
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators, ForgotPasswordPageLocators
from helpers import generate_unique_email, generate_password


class TestLogin:

    @pytest.fixture(autouse=True)
    def create_user(self, driver):
        email = generate_unique_email()
        valid_password, _ = generate_password()
        name = "Тест"
        
        driver.get(Urls.REGISTER_PAGE)
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(valid_password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        
        self.test_email = email
        self.test_password = valid_password

    def test_login_main_button(self, driver):
        """Тест 3: Вход по кнопке «Войти в аккаунт» на главной"""
        driver.get(Urls.MAIN_PAGE)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON_MAIN).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(self.test_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(self.test_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        wait = WebDriverWait(driver, 5)
        order_button = wait.until(EC.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        assert order_button.is_displayed()

    def test_login_personal_account(self, driver):
        """Тест 4: Вход через кнопку «Личный кабинет»"""
        driver.get(Urls.MAIN_PAGE)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(self.test_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(self.test_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        wait = WebDriverWait(driver, 5)
        order_button = wait.until(EC.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        assert order_button.is_displayed()

    def test_login_register_button(self, driver):
        """Тест 5: Вход через кнопку в форме регистрации"""
        driver.get(Urls.REGISTER_PAGE)
        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(self.test_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(self.test_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        wait = WebDriverWait(driver, 5)
        order_button = wait.until(EC.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        assert order_button.is_displayed()

    def test_login_forgot_password(self, driver):
        """Тест 6: Вход через кнопку в форме восстановления пароля"""
        driver.get(Urls.FORGOT_PASSWORD_PAGE)
        driver.find_element(*ForgotPasswordPageLocators.LOGIN_BUTTON_FORGOT).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(self.test_email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(self.test_password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
        wait = WebDriverWait(driver, 5)
        order_button = wait.until(EC.presence_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        assert order_button.is_displayed()