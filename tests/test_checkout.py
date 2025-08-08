from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutStepOnePage, CheckoutStepTwoPage
import pytest

@pytest.fixture
def checkout_pages(driver):
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()
    cart.go_to_checkout()
    return CheckoutStepOnePage(driver), CheckoutStepTwoPage(driver)

@pytest.mark.order(8)
def test_successful_checkout_workflow(checkout_pages, driver):
    checkout_one, checkout_two = checkout_pages
    checkout_one.fill_information("Waskar", "Añil", "10101")
    checkout_two.finish_checkout()
    confirmation_msg = checkout_two.get_confirmation_message()
    assert "Thank you for your order" in confirmation_msg

@pytest.mark.order(7)
def test_checkout_with_empty_info(checkout_pages):
    checkout_one, _ = checkout_pages
    checkout_one.click_continue()
    error_msg = checkout_one.get_error_message()
    assert "First Name is required" in error_msg

@pytest.mark.order(6)
def test_checkout_with_empty_cart(driver):
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()
    inventory = InventoryPage(driver)
    inventory.go_to_cart()
    cart = CartPage(driver)
    cart.go_to_checkout()
    assert "checkout-step-one.html" in driver.current_url