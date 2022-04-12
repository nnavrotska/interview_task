import allure
import pytest
from framework.pages.home_page import HomePage
from framework.pages.register_page import RegisterPage
from framework import config


@pytest.fixture(scope='function')
def home_page(driver):
    return HomePage(driver).load_using_url()


@pytest.fixture(scope='function')
def register_page(driver):
    return RegisterPage(driver).load_using_url()


@allure.step('Set input value {config.VALID_USER_EMAIL}')
@pytest.fixture(scope="function")
def register_user_with_valid_email(register_page):
    register_page.register_user(config.VALID_USER_EMAIL)
    return register_page


@allure.step('Set input value {config.INVALID_USER_EMAIL}')
@pytest.fixture(scope="function")
def register_user_with_invalid_email(register_page):
    register_page.register_user(config.INVALID_USER_EMAIL)
    return register_page
