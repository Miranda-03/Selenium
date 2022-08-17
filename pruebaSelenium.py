from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
urlFormulario = "https://selenium-tp.herokuapp.com/formulario"
urlLogin = "https://selenium-tp.herokuapp.com/login"

try: 
    wait = WebDriverWait(driver, 10)
    driver.get("https://selenium-tp.herokuapp.com/")  

    wait.until(EC.title_is('Home'))


    boton_formulario = driver.find_element((By.ID, "boton-ir-formulario"))
    

    time.sleep(5)
    boton_formulario.send_keys(Keys.ENTER)
        
    get_url = driver.current_url
    print(get_url)

    wait.until(EC.title_is('Formulario'))


    inputs_formulario = driver.find_element(By.ID, "form")
    input_1 = inputs_formulario.find_element(By.ID, "in-1")
    time.sleep(5)
    input_1.send_keys('Agustin')
    time.sleep(3)

finally:
    driver.quit()
