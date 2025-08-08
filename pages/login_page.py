from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def enter_username(self, username):
        self.do_send_keys(self.username_input, username, "ingresar_usuario")

    def enter_password(self, password):
        self.do_send_keys(self.password_input, password, "ingresar_password")

    def click_login(self):
        self.do_click(self.login_button, "clic_en_login")
        
    def get_error_message(self):
        return self.get_text(self.error_message)