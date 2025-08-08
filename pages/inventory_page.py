from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.remove_from_cart_button = (By.ID, "remove-sauce-labs-backpack")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def add_backpack_to_cart(self):
        self.do_click(self.add_to_cart_button, "anadir_mochila_al_carrito")
        
    def remove_backpack_from_cart(self):
        self.do_click(self.remove_from_cart_button, "quitar_mochila_del_carrito")

    def get_cart_items_count(self):
        try:
            return int(self.get_text(self.cart_badge))
        except:
            return 0

    def go_to_cart(self):
        self.do_click(self.cart_icon, "ir_al_carrito")