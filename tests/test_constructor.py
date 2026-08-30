# tests/test_constructor.py — тесты для конструктора

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from data import Urls
from locators import MainPageLocators


class TestConstructor:

    def test_buns_section(self, driver):
        """Тест 11: Переход к разделу «Булки»"""
        driver.get(Urls.MAIN_PAGE)
        driver.find_element(*MainPageLocators.BUNS_SECTION).click()
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_TAB)
        assert "Булки" in active_tab.text

    def test_sauces_section(self, driver):
        """Тест 12: Переход к разделу «Соусы»"""
        driver.get(Urls.MAIN_PAGE)
        driver.find_element(*MainPageLocators.SAUCES_SECTION).click()
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_TAB)
        assert "Соусы" in active_tab.text

    def test_fillings_section(self, driver):
        """Тест 13: Переход к разделу «Начинки»"""
        driver.get(Urls.MAIN_PAGE)
        driver.find_element(*MainPageLocators.FILLINGS_SECTION).click()
        active_tab = driver.find_element(*MainPageLocators.ACTIVE_TAB)
        assert "Начинки" in active_tab.text