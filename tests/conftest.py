import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.base_page import BasePage

@pytest.fixture
def driver(request):
    # Reinicia el contador de capturas para cada nueva prueba
    BasePage.screenshot_counter = 0
    
    options = Options()
    # Configuracion para deshabilitar avisos de contraseñas y ejecutar limpio
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--incognito")
    options.add_argument("--password-store=basic")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-features=PasswordManager,PasswordManagerUI,PasswordSaving,AutofillServerCommunication")
    
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    
    # Guarda el nombre del test actual en la instancia del driver
    driver.test_name = request.node.name
    
    driver.implicitly_wait(5)
    
    yield driver
    
    if request.node.rep_call.failed:
        import os
        failure_screenshots_dir = os.path.join("reports", "failure_screenshots")
        if not os.path.exists(failure_screenshots_dir):
            os.makedirs(failure_screenshots_dir)
        filepath = os.path.join(failure_screenshots_dir, f"{driver.test_name}_failure.png")
        driver.save_screenshot(filepath)

    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)