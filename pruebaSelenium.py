from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability("browserVersion", "67")
chrome_options.set_capability("platformName", "WINDOWS")
driver = webdriver.Remote(
    command_executor='https://' + 'martnmiranda_nBdHPX' + ':' +
    'kiyXF1ubqhXmAhBsidzT' + '@hub-cloud.browserstack.com/wd/hub',
    options=chrome_options
)

urlHome = "https://selenium-tp.herokuapp.com/"
#urlFormulario = "https://selenium-tp.herokuapp.com/formulario"
#urlLogin = "https://selenium-tp.herokuapp.com/login"

try:
    wait = WebDriverWait(driver, 10)
    driver.get(urlHome)

    # ------------ Home (index.html) ------------

    wait.until(EC.title_is('Selenium'))

    boton_formulario = driver.find_element(By.ID, "boton-ir-formulario")

    time.sleep(5)
    boton_formulario.send_keys(Keys.ENTER)

    """
    get_url = driver.current_url
    print(get_url)
    """
    # ------------ Parte del formulario ------------

    wait.until(EC.title_is('Formulario'))

    inputs_formulario = driver.find_element(By.ID, "form")

    input_nombre = inputs_formulario.find_element(By.ID, "in-1")
    input_apellido = inputs_formulario.find_element(By.ID, "in-2")
    input_edad = inputs_formulario.find_element(By.ID, "in-3")

    time.sleep(5)
    input_nombre.send_keys('Agustin')
    time.sleep(1)
    input_apellido.send_keys('Torti')
    time.sleep(1)
    input_edad.send_keys(18)
    time.sleep(2)

    x = driver.find_element(By.ID, "dropdown")
    drop = Select(x)
    drop.select_by_value("Masculino")
    time.sleep(4)

    driver.find_element(By.ID, "boton-formulario").send_keys(Keys.ENTER)
    time.sleep(4)

    driver.find_element(By.TAG_NAME, "a").send_keys(Keys.ENTER)
    time.sleep(5)

    # ------------ Parte del Log in ------------

    wait.until(EC.title_is('Log in'))

    input_usuario = driver.find_element(By.ID, "input-nombre")
    input_contraseña = driver.find_element(By.ID, "input-pass")

    input_usuario.send_keys("alumno")
    time.sleep(1)
    input_contraseña.send_keys(123)
    time.sleep(2)

    driver.find_element(By.ID, "boton-form-login").send_keys(Keys.ENTER)
    time.sleep(3)

    # ------------ Parte de navegación ------------

    driver.find_element(By.ID, "inputBuscador").send_keys("home")
    driver.find_element(By.ID, "boton-buscar").send_keys(Keys.ENTER)

    wait.until(EC.title_is('Selenium'))
    time.sleep(2)

    driver.find_element(By.ID, "inputBuscador").send_keys("formulario")
    driver.find_element(By.ID, "boton-buscar").send_keys(Keys.ENTER)

    wait.until(EC.title_is('Formulario'))
    time.sleep(2)

    driver.find_element(By.ID, "inputBuscador").send_keys("log in")
    driver.find_element(By.ID, "boton-buscar").send_keys(Keys.ENTER)

    wait.until(EC.title_is('Log in'))
    time.sleep(2)

finally:
    driver.quit()
