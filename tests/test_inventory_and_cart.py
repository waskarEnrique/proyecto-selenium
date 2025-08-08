from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest

@pytest.fixture
def inventory_page(driver):
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()
    return InventoryPage(driver)

@pytest.mark.order(4)
def test_add_item_to_cart(inventory_page):
    inventory_page.add_backpack_to_cart()
    count = inventory_page.get_cart_items_count()
    assert count == 1

@pytest.mark.order(5)
def test_remove_item_from_cart(inventory_page):
    inventory_page.add_backpack_to_cart()
    assert inventory_page.get_cart_items_count() == 1
    inventory_page.remove_backpack_from_cart()
    count = inventory_page.get_cart_items_count()
    assert count == 0