from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutStepOnePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def fill_information(self, first_name, last_name, postal_code):
        self.do_send_keys(self.first_name_input, first_name, "llenar_nombre")
        self.do_send_keys(self.last_name_input, last_name, "llenar_apellido")
        self.do_send_keys(self.postal_code_input, postal_code, "llenar_codigo_postal")
        self.do_click(self.continue_button, "clic_en_continuar")

    def click_continue(self):
        self.do_click(self.continue_button, "clic_en_continuar_vacio")
        
    def get_error_message(self):
        return self.get_text(self.error_message)

class CheckoutStepTwoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.finish_button = (By.ID, "finish")
        self.confirmation_header = (By.CLASS_NAME, "complete-header")

    def finish_checkout(self):
        self.do_click(self.finish_button, "clic_en_finalizar")

    def get_confirmation_message(self):
        return self.get_text(self.confirmation_header)