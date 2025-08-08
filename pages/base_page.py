import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    # Contador para nombrar las capturas en orden cronologico
    screenshot_counter = 0

    def __init__(self, driver):
        self.driver = driver
        # Objeto de espera 
        self.wait = WebDriverWait(self.driver, 10)

    def _take_screenshot(self, step_name):
        """Metodo privado para tomar y guardar una captura de pantalla."""

        time.sleep(1)

        base_screenshots_dir = os.path.join("reports", "screenshots")
        test_screenshots_dir = os.path.join(base_screenshots_dir, self.driver.test_name)
        
        if not os.path.exists(test_screenshots_dir):
            os.makedirs(test_screenshots_dir)

        BasePage.screenshot_counter += 1
        filename = f"{BasePage.screenshot_counter:02d}_{step_name}.png"
        filepath = os.path.join(test_screenshots_dir, filename)
        
        self.driver.save_screenshot(filepath)

    def do_click(self, locator, step_name):
        """Espera a que un elemento sea clickeable, le hace clic y toma captura."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        self._take_screenshot(step_name)

    def do_send_keys(self, locator, text, step_name):
        """Espera a que un elemento sea visible, escribe en el y toma captura."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(text)
        self._take_screenshot(step_name)

    def get_text(self, locator):
        """Espera a que un elemento sea visible y devuelve su texto."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text