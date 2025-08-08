from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_button = (By.ID, "checkout")

    def go_to_checkout(self):
        self.do_click(self.checkout_button, "clic_en_checkout")