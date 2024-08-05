import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-extensions')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-browser-side-navigation')
options.add_argument('--disable-gpu')

def take_screenshot(context, step_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    screenshot_name = os.path.join(screenshot_dir, f"{step_name}_{timestamp}.png")
    context.driver.save_screenshot(screenshot_name)
    context.pdf.add_screenshot(screenshot_name, step_name)
    print(f"Screenshot taken: {screenshot_name}")
    return screenshot_name

def mark_step_as_failed(context, step_name, exception):
    print(f"Error in '{step_name}': {exception}")
    raise Exception(f"Step failed: {step_name}. Error: {exception}")

def mark_step_as_passed(context, step_name):
    print(f"Step passed: {step_name}")

@given('Se inicia el navegador')
def iniciarNavegador(context):
    context.driver = webdriver.Chrome(options=options)
    context.failed_steps = []
    print("Browser started")

@when('Entra a la seccion vehiculo')
def asignar(context):
    try:
        context.driver.maximize_window()
        context.driver.get("C:\\Users\\Ariel\\OneDrive\\Documentos\\QUINTOSEMESTRE\\Requisitos\\Maquetados\\Vehiculo\\Vehiculo.html")
        take_screenshot(context, '1. Entra a la seccion vehiculo')
        print("Entered 'Asignar' option")
    except Exception as e:
        mark_step_as_failed(context, 'entra_opcion_asignar', e)

@when('Busca Vehiculo a Visualizar {placa}')
def escogerChofer(context,placa):
    try:
        select_element = context.driver.find_element(By.XPATH, '//*[@id="nombre"]')
        select_element.send_keys(placa)  # Seleccionar por texto visible
        take_screenshot(context, '2. Buscar Vehiculo a eliminar')
        print(f"Selected drive")
    except Exception as e:
        mark_step_as_failed(context, 'escoge_chofer', e)
