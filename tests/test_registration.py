# tests/test_registration.py — тесты для регистрации

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from data import Urls
from locators import RegisterPageLocators, LoginPageLocators
from helpers import generate_unique_email, generate_password


class TestRegistration:

    def test_successful_registration(self, driver):
        """Тест 1: Успешная регистрация"""
        email = generate_unique_email()
        valid_password, _ = generate_password()
        name = "Тест"
        
        driver.get(Urls.REGISTER_PAGE)
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(valid_password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        
        wait = WebDriverWait(driver, 5)
        login_button = wait.until(EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        assert login_button.is_displayed()

    def test_registration_invalid_password(self, driver):
        """Тест 2: Ошибка для некорректного пароля (менее 6 символов)"""
        email = generate_unique_email()
        _, invalid_password = generate_password()
        name = "Тест"
        
        driver.get(Urls.REGISTER_PAGE)
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(invalid_password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        
        wait = WebDriverWait(driver, 5)
        error_message = wait.until(EC.presence_of_element_located(RegisterPageLocators.ERROR_MESSAGE))
        assert error_message.is_displayed()