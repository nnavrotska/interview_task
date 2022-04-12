import allure
import pytest


@pytest.mark.skip(reason='priority_low')
@allure.step("Verify title of the home page")
def test_home_page_url_title(home_page):
    assert home_page.get_title() == 'My Store'


@pytest.mark.button
@allure.step('Verify "Sign In" button name.')
def test_sign_in_btn_text(home_page):
    assert home_page.sign_in_btn.get_text().strip() == 'Sign in'
