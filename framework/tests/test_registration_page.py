import allure
import pytest


@allure.step("Verify title of the register page")
def test_register_page_url_title(register_page):
    assert register_page.get_title() == 'Login - My Store'


@pytest.mark.button
@allure.step('Verify "Create an account" button name.')
def test_create_an_account_btn_text(register_page):
    assert register_page.create_an_account_btn.text == 'Create an account'


@pytest.mark.register_page
def test_create_an_account_with_invalid_email(register_user_with_invalid_email):
    assert register_user_with_invalid_email.get_warning_message() == 'Invalid email address.'


@pytest.mark.register_page
def test_create_an_account_with_valid_email(register_user_with_valid_email):
    assert register_user_with_valid_email.get_current_url() == 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
