from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

desired_cap = {
    'browser': 'Chrome',
    'browser_version': '84.0 beta',
    'os': 'OS X',
    'os_version': 'Catalina',
    'resolution': '1024x768',
    'name': 'Bstack-[Python] Sample Test'
}

driver = webdriver.Remote(
        command_executor='kiyXF1ubqhXmAhBsidzT',
        desired_capabilities=desired_cap
    )
driver.get('https://selenium-tp.herokuapp.com/')