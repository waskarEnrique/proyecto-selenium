from pages.login_page import LoginPage
import pytest

@pytest.fixture
def login_page(driver):
    driver.get("https://www.saucedemo.com/")
    return LoginPage(driver)

@pytest.mark.order(1)
def test_successful_login(login_page, driver):
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    assert "inventory.html" in driver.current_url

@pytest.mark.order(2)
def test_locked_out_user_login(login_page):
    login_page.enter_username("locked_out_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    error_msg = login_page.get_error_message()
    assert "user has been locked out" in error_msg

@pytest.mark.order(3)
def test_login_with_empty_credentials(login_page):
    login_page.click_login()
    error_msg = login_page.get_error_message()
    assert "Username is required" in error_msg