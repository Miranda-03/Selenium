from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability("browserVersion", "67")
chrome_options.set_capability("platformName", "WINDOWS")
driver = webdriver.Remote(
     command_executor='https://'+ 'martnmiranda_nBdHPX' + ':' + 'kiyXF1ubqhXmAhBsidzT' + '@hub-cloud.browserstack.com/wd/hub',
    options=chrome_options
)
driver.get("https://selenium-tp.herokuapp.com/")

el = WebDriverWait(driver, timeout=3).until(lambda driver: driver.find_element(By.ID, "boton-ir-formulario").send_keys(Keys.ENTER))

driver.quit()  